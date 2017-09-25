# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

import math
from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    def __init__(self,x,y):
        angle = 2*math.pi*random()
        self._color = "#ff0000"
        width = Floater.radius*2
        height = width
        Prey.__init__(self,x,y,width,height,angle,5)

    def update(self):
        chance = random()
        if chance < 0.3:
            angle = self.get_angle()
            speed = self.get_speed()
            angle_delta = random() - 0.5
            speed_delta = random() - 0.5
            self.set_angle(angle + angle_delta)
            speed = speed + speed_delta
            if speed < 3:
                speed = 3
            if speed > 7:
                spped = 7
            self.set_speed(speed)
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-Floater.radius,
            y-Floater.radius,
            x+Floater.radius,
            y+Floater.radius,
            fill=self._color)

    