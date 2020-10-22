# A Hunter is both a  Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    def __init__(self,x,y):
        self.count = 0
        self.randomize_angle()
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,self.radius*2,self.radius*2,self.get_angle(),5)
    
    def update(self, model):
        from blackhole import Black_Hole
        if self.radius == 0:
            model.remove(self)
        self.count += 1
        self.move()
        self.wall_bounce()
        target = None
        target_set = set()
        for i in model.balls:
            if self.distance(i.get_location()) <= 400 and type(i) is not Black_Hole and type(i) is not Pulsator and type(i) is not Hunter:
                target_set.add(i)
        if target_set != set():
            target = sorted(target_set, key = lambda x: self.distance(x.get_location()))[0]
            self.set_angle(atan2(target._y - self._y, target._x - self._x))
        eaten = model.find(self.contains)
        for i in eaten:
            self.radius += .5
            model.remove(i)
        if self.count == 30:
            self.radius -= .5
            self.count = 0
        return eaten