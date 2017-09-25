# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

import model
from prey import Prey
from blackhole import Black_Hole


class Pulsator(Black_Hole):
    MAX_COUNTER = 30
    def __init__(self, x, y):
        self.counter = 0
        Black_Hole.__init__(self,x,y)

    def update(self):
        eaten_prey = set()
        self.counter += 1
        # find all preys
        preys = model.find(lambda x:isinstance(x, Prey))
        # filter preys, find prey, find eaten prey
        for prey in preys:
            xy = prey.get_location()
            if self.contains(xy):
                self.change_dimension(1, 1)
                self.counter = 0
                self.radius += 1
                eaten_prey.add(prey)
        if self.counter >= self.MAX_COUNTER:
            self.change_dimension(-1, -1)
            self.radius += -1
            self.counter = 0
            if self.radius <= 0:
                eaten_prey.add(self)
        return eaten_prey


