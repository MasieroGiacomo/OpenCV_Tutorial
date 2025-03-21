import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

# Create a rectangle onto a copy of blank.                              
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)     # Can use 255 since binary (=>white), -1 to fill inside
# Create a circle 
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
# Show the results
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

## AND ##

# (source im1, source im2)      Returns intercepting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('AND', bitwise_and)

## OR ##

# (source im1, source im2)      Returns both intersecting and not intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or)

## XOR ##

# (source im1, source im2)      Returns not intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_xor)

## NOT ##

# (source im)                   Invert binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_not)

cv.waitKey(0)