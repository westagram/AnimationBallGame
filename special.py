# A Special (aka HeroMouse) acts like a Hunter, but it 
#    only hunts down the UFO(Floater), blackholes and 
#    pulsators. HeroMouse changes its angel to a random angle every 10 cycle count 
#    HeroMouse uses the furthest Ball object to blink to every time
#    there is a Hunter near by (50 radius). Once HeroMouse
#    blinks, it will change to a different angle and its
#    speed will increase by .5 (max speed: 7).


#from PIL.ImageTk import PhotoImage
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Special(Pulsator,Mobile_Simulton):
    radius = 10
    
    def __init__(self,x,y):
        #self._image = PhotoImage(file='mouse.gif')
        self.count = 0
        self.randomize_angle()
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,self.radius*2,self.radius*2,self.get_angle(),5)
    
    def update(self, model):
        import random
        from ball import Ball
        from hunter import Hunter
        if self.radius == 0:
            model.remove(self)
        self.count += 1
        if self.count == 10:
            self.count = 0
            self.set_angle(self.get_angle() + random.uniform(-.5, .5))
        self.move()
        self.wall_bounce()
        target, hiding = None, None
        target_set, hiding_set, running_set = set(), set(), set()
        for i in model.balls:
            if self.distance(i.get_location()) <= 400 and type(i) is not Ball and type(i) is not Hunter and type(i) is not Special:
                target_set.add(i)
            if self.distance(i.get_location()) <= 500 and type(i) is Ball:
                hiding_set.add(i)
            if self.distance(i.get_location()) <= 50 and type(i) is Hunter:
                running_set.add(i)
        if hiding_set != set():
            hiding = sorted(hiding_set, key = lambda x: self.distance(x.get_location()))[-1]
        if running_set != set():
            if hiding_set != set():
                self.set_location(hiding.get_location()[0], hiding.get_location()[1])
                self.randomize_angle()
                if self.get_speed() < 7:
                    self.set_speed(self.get_speed() + .5)
        if target_set != set():
            target = sorted(target_set, key = lambda x: self.distance(x.get_location()))[0]
            self.set_angle(atan2(target._y - self._y, target._x - self._x))
        for i in target_set:
            if self.contains(i):
                model.remove(i)
    
    def display(self,the_canvas):
        #the_canvas.create_image(*self.get_location())#,image=self._image)
        the_canvas.create_oval(self._x - Special.radius, self._y - Special.radius,
                           self._x + Special.radius, self._y + Special.radius, fill = 'green')


