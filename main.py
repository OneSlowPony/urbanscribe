# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import sys
import json


def prettyJSON(d):
    return json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

imagePath = "images/jake.jpg"

track = "faces"

# load the image and resize it to (1) reduce detection time
# and (2) improve detection accuracy

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

aspectRatio = float(16)/9
imageWidth = 600
imageHeight = imageWidth / aspectRatio


while True:
    ret, frame = video_capture.read()
    image = imutils.resize(frame, width=min(imageWidth, frame.shape[1]))
    orig = image.copy()

    if track == "faces":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        rects = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
    elif track == "people":
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    for r in rects:
        rect = {
            "position": {
                "x": float(r[0] + r[2]) / 2 / imageWidth,
                "y": float(r[1] + r[3]) / 2 / imageHeight
            },
            "size":{
                "x": float(r[2] - r[0]) / imageWidth,
                "y": float(r[3] - r[1]) / imageHeight
            }
        }
        print(prettyJSON(rect))

    # show some information on the number of bounding boxes
    # filename = imagePath[imagePath.rfind("/") + 1:]

    #print("{} original boxes, {} after suppression".format(len(rects), len(pick)))
    # Display the resulting frame
    cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

# show the output images
# cv2.imshow("Before NMS", orig)
# cv2.imshow("After NMS", image)
# cv2.waitKey(0)
