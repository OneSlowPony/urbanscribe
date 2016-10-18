import math
from geometric_algorithm import *

for length in range(1, 15):
    # print("//////")
    print(length, coordsToAngles({
        "x": length,
        "y": 0
    }))
