# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a _radius
#   of 5 (width/height 10).

import math
from random import random
from prey import Prey


class Ball(Prey):
    _radius = 5
    def __init__(self,x,y):
        self._color =  "#0000ff"
        width = Ball._radius*2
        height = Ball._radius*2
        angle = 2*math.pi*random()
        Prey.__init__(self, x,y,width,height,angle,5)

    def update(self):
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-self._radius,y-self._radius,x+self._radius,y+self._radius,fill=self._color)
