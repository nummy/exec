# Put imports here
from random import random
from nearestneighbor import closest_2d
from performance import Performance

# Put code for performance analysis here 
def setup(size):
    global alist
    alist = [(random(),random()) for i in range(size)]
        
def code():
    global alist
    closest_2d(alist)


for i in range(0,9):
    size = 100 * 2**i
    p = Performance(lambda : code(), lambda:setup(size),5,'\n\nNearest Neighbor, size = ' + str(size))
    p.evaluate()
    p.analyze()
 