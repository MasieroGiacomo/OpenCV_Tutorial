import cv2 as cv
import numpy as np


## CREATE A BLANK IMAGE ##
# (width, height, # of color channels ONLY if put colors).  uint8 is the datatype of an image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

## PAINT THE BLANK IMAGE ##
'''
# Select all/some pixels of the blank and color them    ! BLUE GREEN RED !
blank[:] = 0,255,0
cv.imshow('Green', blank)
blank[300:400, 300:400] = 255,0,0
cv.imshow('Blue Square', blank)
'''

## DRAW A RECTANGLE ##
'''
# (image to draw on, (starting point), (endpoint), (color), thickness)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)       # Just the shape
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)      # Color inside the shape
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)      # 
cv.imshow('Rectangle', blank)
'''

## DRAW A CIRCLE ##
'''
# (image to draw on, (center), radius, (color), thickness)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3)
cv.imshow('Circle', blank)
'''

## DRAW A LINE ##
'''
# (image to draw on, (begin point), (end point), (color), thickness)
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)
'''

## ADD TEXT ##
'''
# (image to write on, 'Text', (origin point), font, scale, (color), thickness)
# ! No way to do it if the text goes offscreen !
cv.putText(blank, 'Hello! It works', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow('Text', blank)
'''

cv.waitKey(0)  