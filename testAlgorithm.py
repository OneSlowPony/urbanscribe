from __future__ import print_function


import math
from geometric_algorithm import *
for y in range(0,10):
    for x in range(0, 10):
        a1,a2 = coordsToAngles({
            "x": x,
            "y": y
        })

        print("(" + str(int(a1)) + "," + str(int(a2))+")  ", end="") 
    print()

