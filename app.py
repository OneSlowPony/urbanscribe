#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2

# import the necessary packages
#from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import sys
import json
import math


thing = "Hello"

def prettyJSON(d):
    return json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

app = Flask(__name__)
vc = cv2.VideoCapture(0)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    while True:
        print(thing)
        rval, frame = vc.read()
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/kill')
def kill():
    exit()
# @app.route('/data')
# def get_data():
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
