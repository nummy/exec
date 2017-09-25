# A Black_Hole is derived from only a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter
import model
from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self, x, y):
        self._color = "#000000"
        width = Black_Hole.radius*2
        height = width
        Simulton.__init__(self,x,y,width,height)

    def update(self):
        result = set()
        objs = model.find(lambda x:isinstance(x, Prey))
        for obj in objs:
            xy = obj.get_location()
            if self.contains(xy):
                result.add(obj)
        return result

    def display(self, canvas):
        x, y = self.get_location()
        canvas.create_oval(x-self.radius,
            y-self.radius,
            x+self.radius,
            y+self.radius,
            fill=self._color)


    def contains(self, xy):
        x,y = self.get_location()
        return ((xy[0]-x)**2 + (xy[1]-y)**2)**.5 < self.radius

