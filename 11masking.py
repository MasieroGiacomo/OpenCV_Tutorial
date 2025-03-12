import cv2 as cv
import numpy as np

# Masking allows to focus on certain parts of the image
# ! The mask must have the same dimensions as the image !

img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# Create the mask, in this case a circle in the center of the image
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 50, 255, -1)
cv.imshow('Mask', mask)

# Mask the image        ! Put img as bot sources !
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)


cv.waitKey(0)