import cv2 as cv
import numpy as np

## Contours != Edges froma mathematical POV

img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
# Convert the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1.GRAB THE EDGES USING CANNY
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)
# contours: list off all coordinates of contours, hierarchies: hierarchical representation of contours
# Modes: RETR_TREE => All hierarchical contours, RETR_EXTERNAL => Only external contours, RETR_LIST => All contours     
# Method: How to approx the contours. NONE: does nothing, SIMPLE: compress all into simple ones (ex: line -> two endpoints)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Can print the lenght of this list to see how many contours
print(f'{len(contours)} contour(s) found!')


# 2. USING ThRESHOOLD METHOD
# Pixel value < 125 => black    pixel value > 255 => white.  THRESH_BINARY because I'm binarizing the image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# Can print the lenght of this list to see how many contours
print(f'{len(contours)} contour(s) found!')


## DRAW CONTOURS ON A BLANK IMAGE ##

# image to draw on, contours (list), how many you want (-1 => all), color, thicness
cv.drawContours(blank, contours, -1, (255,0,0), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)
