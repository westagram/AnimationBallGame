# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self,x,y,Ball.radius*2,Ball.radius*2, self.get_angle(),5)
    
    def update(self, model):
        self.move()
        self.wall_bounce()
    
    def display(self, canvas):
        canvas.create_oval(self._x - Ball.radius, self._y - Ball.radius,
                           self._x + Ball.radius, self._y + Ball.radius, fill = 'blue')