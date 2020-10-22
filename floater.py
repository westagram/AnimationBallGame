# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random

class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        #self._image = PhotoImage(file='ufo.gif')
        self.randomize_angle()
        Prey.__init__(self,x,y,Floater.radius*2,Floater.radius*2, self.get_angle(),5)
    
    def update(self, model):
        self.move()
        self.wall_bounce()
        rand_int = random.randint(0,10)
        if rand_int <= 3:
            self.set_angle(self.get_angle() + random.uniform(-.5, .5))
            while True:
                n = random.uniform(-.5, .5)
                if (self.get_speed() + n) < 7 or (self.get_speed() + n) > 3:
                    self.set_speed(self._speed+n)
                    break
    
    def display(self,the_canvas):
        #the_canvas.create_image(*self.get_location())#,image=self._image)
        the_canvas.create_oval(self._x - Floater.radius, self._y - Floater.radius,
                           self._x + Floater.radius, self._y + Floater.radius, fill = 'red')
