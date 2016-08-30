# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import sys
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, image = video_capture.read()

    image = imutils.resize(image, width=min(300, image.shape[1]))
    orig = image.copy()

    # detect people in the image
    (people, weights) = hog.detectMultiScale(image, winStride=(4, 4),
        padding=(8, 8), scale=1.05)

    # Detect faces
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    objects = faces

    # draw the original bounding boxes
    for (x, y, w, h) in objects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    objects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in objects])
    pick = non_max_suppression(objects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)


    print(" {} original boxes, {} after suppression".format(len(objects), len(pick)))


    cv2.imshow('Video', image)

    # if cv2.waitKey(1) & 0xFF == 113: # This is q
    #     break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()