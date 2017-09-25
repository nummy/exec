# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

import math
from random import random
from PIL.ImageTk import PhotoImage
from prey import Prey



class Floater(Prey):
    def __init__(self,x,y):
        self._image = PhotoImage(file='ufo.gif')
        width = self._image.width()
        height = self._image.height()
        angle = 2*math.pi*random()
        Prey.__init__(self,x,y,width,height,angle,5)

    def update(self):
        prob = random()
        if prob < 0.3:
            angle_var = random() - 0.5
            speed_var = random() - 0.5
            self.set_angle(self.get_angle() + angle_var)
            speed = self.get_speed() + speed_var
            if speed > 7:
                spped = 7
            if speed < 3:
                speed = 3
            self.set_speed(speed)
        self.move()
        self.wall_bounce()

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_image(*self.get_location(),image=self._image)

    