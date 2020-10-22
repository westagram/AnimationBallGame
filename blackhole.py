# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    
    def __init__(self,x,y):
        self.radius = 10
        Simulton.__init__(self,x,y,self.radius*2,self.radius*2)
    
    def update(self, model):
        from special import Special
        eaten = model.find(self.contains)
        for i in eaten:
            if type(i) is not Special:
                model.remove(i)
        return eaten
            
    def display(self, canvas):
        canvas.create_oval(self._x - self.radius, self._y - self.radius,
                           self._x + self.radius, self._y + self.radius, fill = 'black')
        
    def contains(self,xy):
        if type(xy) is tuple:
            return self._x - self._width/2  <= xy[0] <= self._x + self._width/2 and\
               self._y - self._height/2 <= xy[1] <= self._y + self._height/2
        else:
            return self._x - self.radius  < xy._x < self._x + self.radius and\
                self._y - self.radius < xy._y < self._y + self.radius