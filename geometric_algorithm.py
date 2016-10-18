import math

def findAngle(x,y):
    if(x==0 and y==0):
        return 0
    elif(x==0):
        return 90
    elif(y==0):
        return 0
    else:
        return math.degrees(math.atan(y/x))

def coordsToAngles(position):
    x = position["x"]
    y = position["y"]

    segmentLength = 5

    radius = math.sqrt(x**2+y**2)
    #initialBaseAngle = math.degrees(math.atan(position["y"] / (position["x"]+0.001)))

    if(radius > 2* segmentLength):
        #print("Arm not long enough!")
        return [-1,-1]

    # The magic happens here
    mainAngle = math.degrees(
        math.acos(
            1 - radius**2.0 / (2.0 * segmentLength**2.0)
        )
    )

    mainServo = (mainAngle / 2.0) + findAngle(x,y)
    subServo = mainAngle  # 180 -

    return [mainServo, subServo]

