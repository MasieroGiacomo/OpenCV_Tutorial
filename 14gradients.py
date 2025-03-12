import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')
#cv.imshow('Cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

## 1. LAPLACIAN ##

# Compute the gradient of the gray image (when transition from black to white=> positive slope, else negative)
# Images can't have negative pixel values, so we use the absolute value and then we convert that to uint8 (image data type)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) 
cv.imshow('Laplacian', lap)

## SOBEL GRADING MAGNITUDE REPRESENTATION ##

# Computes the gradient in two directions (x,y) 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sovel', combined_sobel)

## COMPARISON OF LAPLACIAN, SOBEL AND CANNY METHODS ##

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

# Canny is the more advanced algorithm, that draw the edges better and it's used in most of the times


cv.waitKey(0)