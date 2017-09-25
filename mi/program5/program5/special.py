# A Special is Prey; it updates change its radius, randomly

import math
import random
from prey import Prey


class Special(Prey):
    def __init__(self,x,y):
        self.counter = 0
        self.radius = 8
        angle = 2*math.pi*random.random()
        self._color =  "#00ffff"
        width = self.radius*2
        height = self.radius*2
        Prey.__init__(self, x,y,width,height,angle,5)

    def update(self):
        self.counter += 1
        if self.counter == 30:
            delta = random.randint(-8,8)
            self.radius = self.radius + delta
            if self.radius <= 0:
                self.radius = 1
            if self.radius > 12:
                self.radius = 10
            self.counter = 0
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-self.radius,
            y-self.radius,
            x+self.radius,
            y+self.radius,
            fill=self._color)
