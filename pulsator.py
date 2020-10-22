# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    
    def __init__(self,x,y):
        self.count = 0
        Black_Hole.__init__(self,x,y)
     
    def update(self, model):
        from special import Special
        if self.radius == 0:
            model.remove(self)
        self.count += 1
        eaten = model.find(self.contains)
        for i in eaten:
            if type(i) is not Special:
                self.count = 0
                self.radius += .5
                model.remove(i)
        if self.count == 30:
            self.radius -= .5
            self.count = 0
        return eaten