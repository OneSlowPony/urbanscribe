# import numpy as np
# import cv3
# import cv2

# im = cv3.imread('snap.jpg')
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


import cv2
import numpy as np

img = cv2.imread('snap.jpg')
px = img[100,100]


ball = img[0:0, 300:300]
img[300:300, 600:600] = ball

img2 = img

img2[:,:,2] = 255

# b,g,r = cv2.split(img)
# img2 = cv2.merge((b,g,r))

cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()