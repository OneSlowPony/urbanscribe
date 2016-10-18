import math


def coordsToAngles(position):

    segmentLength = 7.0
    maxLength = segmentLength * 2
    radius = position["x"] #**2 + position["y"]**2
    initialBaseAngle = math.degrees(math.atan(position["y"] / (position["x"]+0.001)));

    #print("Initial base angle", initialBaseAngle)
    # print("using cos")

    # print(math.acos(position["x"]/maxLength))

    # print("Using sin")

    # print(math.acos(position["y"]/maxLength))

    if(radius > 2* segmentLength):
        print("Arm not long enough!")
        return [-1,-1]

    # The magic happens here
    mainAngle = math.degrees(
        math.acos(
            1 - radius**2.0 / (2.0 * segmentLength**2.0)
        )
    )

    mainServo = 90 - (mainAngle / 2.0)
    subServo = mainAngle  # 180 -

    return [mainServo, subServo]


for length in range(0, 15):
    #print("//////")
    print(length, coordsToAngles({
        "x": length,
        "y": 0
    }))
