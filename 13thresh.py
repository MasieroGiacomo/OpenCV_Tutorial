import cv2 as cv

## Thresholding is the binaryzation of an image: we take an image and convert it to a binary image,
# where the pixels are either black (0) or white (255). 
# In practice, a thresh value is defined: if the pixel value is below this thres, the pixel gets 0, else it gets 255

img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)
# Need to get the grey scale image for simple thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## 1. SIMPLE THRESHOLDING ##

# (source img, thresh value, max value, type)
# If pixel value > thresh => pixel -> maxValue, else pixel -> 0
# threshold is the thresh value, thresh is the new image
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Can also do inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

## 2. ADAPTIVE THRESHOLDING ##

# Let the computer find the optimal thresh value and use it
# (source img, max value, adaptive method, thresh type (mean, gaussian...), blocksize, C (for fine tuning, higher => better features))
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3,)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey(0)