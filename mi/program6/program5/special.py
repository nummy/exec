# A Shining prey, it change it's color when updates

import math
import random
from prey import Prey


class Special(Prey):
    def __init__(self,x,y):
        self.radius = 5
        angle = 2*math.pi*random.random()
        self._color =  "#00ffff"
        width = self.radius*2
        height = self.radius*2
        Prey.__init__(self, x,y,width,height,angle,5)

    def update(self):
        self._color = self.random_color()
        self.move()
        self.wall_bounce()

    def random_color(self):
        r = self.convert_to_hex(random.randint(0,255))
        g = self.convert_to_hex(random.randint(0,255))
        b = self.convert_to_hex(random.randint(0,255))
        rgb = "#" + r + g + b
        return rgb

    def convert_to_hex(self, integer):
        res = hex(integer)[2:]
        if len(res) == 1:
            res = "0" + res
        return res

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-self.radius,
            y-self.radius,
            x+self.radius,
            y+self.radius,
            fill=self._color)
 