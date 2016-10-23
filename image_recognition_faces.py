from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import sys
import json
import math
import cv2

# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

aspectRatio = float(16)/9
imageWidth = 600 
imageHeight = imageWidth / aspectRatio


def recognisePeople(image):
    #track = "faces"
    imageCopy = image.copy()
    # Resize
    image = imutils.resize(image, width=min(imageWidth, image.shape[1]))
    image = cv2.flip(image,1)

    # Comment here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Or here!
    # (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
    #                                             padding=(8, 8), scale=1.05)
    # for (x, y, w, h) in rects:
    #     cv2.rectangle(imageCopy, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.1)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    data = []
    for r in rects:
        rect = {
            "position": {
                "x": float(r[0] + r[2]) / 2 / imageWidth,
                "y": float(r[1] + r[3]) / 2 / imageHeight
            },
            "size": {
                "x": float(r[2] - r[0]) / imageWidth,
                "y": float(r[3] - r[1]) / imageHeight
            }
        }
        data.append(rect)
        # print(prettyJSON(rect))
    return image, data
