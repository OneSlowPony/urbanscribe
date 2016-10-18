import math


def coordsToAngles(position):
    maxRadius = position["x"]
    segmentLength = 7
    if(maxRadius > 2* segmentLength):
        print("Arm not long enough!")
        return [-1,-1]

    # The magic happens here
    mainAngle = math.degrees(
        math.acos(
            1 - maxRadius**2.0 / (2.0 * segmentLength**2.0)
        )
    )

    mainServo = 90 - (mainAngle / 2.0)
    subServo = mainAngle  # 180 -

    return [mainServo, subServo]


for length in range(0, 16):
    print(length, coordsToAngles({
        "x": length,
        "y": 0
    }))
