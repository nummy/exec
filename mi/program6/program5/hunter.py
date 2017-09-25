# A Hunter is derived from both a Mobile_Simulton and a Pulsator; it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.

import math
from random import random
from math import atan2
import model
from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton


class Hunter(Pulsator,Mobile_Simulton):
    MAX_DISTANCE = 200
    def __init__(self, x, y):
        width = self.radius*2
        height = self.radius*2
        angle = 2*math.pi*random()
        speed = 5
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self,x,y,width,height,angle,speed)

    def update(self):
        # find all preys
        preys = model.find(lambda simulton:isinstance(simulton, Prey))
        target_preys = []
        distances = []
        # find preys within the distance
        for prey in preys:
            xy = prey.get_location()
            distance = self.distance(xy)
            if distance < self.MAX_DISTANCE:
                distances.append(distance)
                target_preys.append(prey)
        # change direction to the target prey
        if len(target_preys) > 0:
            min_distance = min(distances)
            index = distances.index(min_distance)
            prey = target_preys[index]
            x1,y1 = self.get_location()
            x2,y2 = prey.get_location()
            Mobile_Simulton.set_angle(self, atan2(y2-y1,x2-x1))
        Mobile_Simulton.move(self)
        return Pulsator.update(self)


