# A Hunter is derived from both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.

import model
from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import math
import random


class Hunter(Pulsator,Mobile_Simulton):
    DISTANCE = 200
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        width = self.radius*2
        height = width
        angle = 2*math.pi*random.random()
        speed = 5
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)

    def update(self):
        preys = model.find(lambda x:isinstance(x, Prey))
        targets = []
        distances = []
        for prey in preys:
            xy = prey.get_location()
            distance = self.distance(xy)
            if distance < self.DISTANCE:
                targets.append(prey)
                distances.append(distance)
        if len(targets) != 0:
            min_distance = min(distances)
            index = distances.index(min_distance)
            target = targets[index]
            x1,y1 = self.get_location()
            x2,y2 = target.get_location()
            angle = atan2(y2-y1,x2-x1)
            Mobile_Simulton.set_angle(self, angle)
        Mobile_Simulton.move(self)
        return Pulsator.update(self)


