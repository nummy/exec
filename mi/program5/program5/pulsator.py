# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions

import model
from prey import Prey
from blackhole import Black_Hole


class Pulsator(Black_Hole):
    MAX_COUNT = 30
    def __init__(self, x, y):
        self.counter = 0
        Black_Hole.__init__(self,x,y)

    def update(self):
        result = set()
        self.counter += 1
        objs = model.find(lambda x:isinstance(x, Prey))
        for obj in objs:
            xy = obj.get_location()
            if self.contains(xy):
                result.add(obj)
                self.counter = 0
                self.change_dimension(1, 1)
                self.radius += 1
        if self.counter >= self.MAX_COUNT:
            self.counter = 0
            self.change_dimension(-1, -1)
            self.radius += -1
            w,h = self.get_dimension()
            if self.radius <= 0:
                result.add(self)
        return result


