import math


def findAngle(x,y):
    if(x==0):
        return y
    elif(y==0):
        return x
    else:
        return math.degrees(y/x)




print(findAngle(1,1))