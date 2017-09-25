# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

import math
import random
from prey import Prey


class Ball(Prey):
    radius = 5
    def __init__(self,x,y):
        angle = 2*math.pi*random.random()
        self._color =  "#0000ff"
        width = Ball.radius*2
        height = Ball.radius*2
        Prey.__init__(self, x,y,width,height,angle,5)

    def update(self):
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Ball.radius,
            y-Ball.radius,
            x+Ball.radius,
            y+Ball.radius,
            fill=self._color)
