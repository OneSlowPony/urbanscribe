import math


def findAngle(x,y):
    if(x==0):
        return math.radians(90)
    elif(y==0):
        return math.radians(0)
    else:
        return math.atan(y/x)




print(findAngle(0,1))
print(math.degrees(findAngle(0,1)))