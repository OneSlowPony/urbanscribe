#!/usr/bin/env python
from flask import Flask, render_template, Response, g
from image_recognition import *
from geometric_algorithm import *
import os

def prettyJSON(d):
    return json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

app = Flask(__name__)
vc = cv2.VideoCapture(0)

latestData = []

lastMainServo = 90
lastSubServo = 180

def getPersonSize(p):
    return p["size"]["y"]

def rawDataToAngles(data):
    arrayLength = len(data)
    bestCandidate = {}

    if(arrayLength == 0):
        return -1, -1
    elif(arrayLength > 1):
        bestSize = 0
        for o in data:
            if(getPersonSize(o) > bestSize):
                bestSize = getPersonSize(o)
                bestCandidate = o
    elif(arrayLength == 1):
        bestCandidate = data[0]


    factor = 10
    realPosition = {
        "x": bestCandidate["position"]["x"] * factor,
        "y": bestCandidate["position"]["y"] * factor
    }



    mainServoAngle, subServoAngle = coordsToAngles(realPosition)
    return int(mainServoAngle), int(subServoAngle)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        rval, frame = vc.read()
        peopleImage, data = recognisePeople(frame)
        global latestData
        latestData = data

        # mainServo, subServo = getCurrentServoPositions();
        # print("Main servo: " + str(mainServo) + " subservo: " + str(subServo))

        cv2.imwrite('t.jpg', peopleImage)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def getCurrentServoPositions():
    mainServo, subServo = rawDataToAngles(latestData)

    if(mainServo > 180 or subServo > 180):
        printf("ONE OF THE SERVOS OUT OF BOUNDS")

    global lastMainServo
    global lastSubServo

    if(mainServo == -1):
        mainServo = lastMainServo
        subServo = lastSubServo
    else:
        lastMainServo = mainServo
        lastSubServo = subServo
    return mainServo, subServo

@app.route('/data')
def getData():
    mainServo,subServo = getCurrentServoPositions()
    print("Final: " + str(mainServo) + ", " + str(subServo) + "\n")
    return str(mainServo) + "\n" + str(subServo) + "\n"

@app.route('/kill')
def kill():
    vc.release()
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
