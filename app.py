#!/usr/bin/env python
from flask import Flask, render_template, Response, g
from image_recognition import *
import os

def prettyJSON(d):
    return json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

app = Flask(__name__)
vc = cv2.VideoCapture(0)

latestData = []
lastX = 0
lastY = 0


@app.route('/')
def index():
    return render_template('index.html')

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = vc.read()
        peopleImage, data = recognisePeople(frame)
        global latestData
        latestData = data
        cv2.imwrite('t.jpg', peopleImage)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def getData():
    return prettyJSON(latestData)

@app.route('/kill')
def kill():
    vc.release()
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
