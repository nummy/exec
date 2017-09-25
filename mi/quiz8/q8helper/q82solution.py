# Put imports here
import cProfile
import pstats
from random import random
from nearestneighbor import closest_2d

# Put code for profile analysis here 
alist = [(random(), random()) for i in range(25600)]
cProfile.run('closest_2d(alist)', "output")
p = pstats.Stats("output")
p.sort_stats("ncalls").print_stats(15)
p.sort_stats("tottime").print_stats(15)