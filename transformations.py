import cv2 as cv
import numpy as np

img = cv.imread('Images/FaticaNeiMateriali.png')
cv.imshow('OG', img)

## TRANSLATION (X,Y) ##

# X => Right    Y=> Down 
# (source image, x, y)
def translate(img, x, y):
    # Create a transformation matrix [1 0 x     1 on diag => no scale  
    #                                 0 1 y] 
    transMatrix = np.float32([[1,0,x], [0,1,y]])                
    # Get the width and height of the original image
    dimensions = (img.shape[1], img.shape[0])
    # Transform the img with the matrix
    return cv.warpAffine(img, transMatrix, dimensions) 

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

## ROTATION ##

# Positive Angle => CCW
# (source image, angle, center)
def rotate(img, angle, rotPoint=None):
    # Get height, width of the image by picking the first two values of shape
    (height, width) = img.shape[:2]
    # If the rotPoint is not chosen, assume it's the center
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    # Create a rotational matrix (center, angle, scale)
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    # Get dimensions in an array
    dimensions = (width, height)
    # Return the rotated image 
    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, 20.0)
cv.imshow('Rotated', rotated)

## RESIZE ##

# (source, newDimensions, type of interpolation)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# INTER_AREA if shrinking, INTER_LINEAR / CUBIC if enlarging
cv.imshow('Resized', resized)

## FLIP ##

#(source image, flip code) --> 0 => flip wrt X, 1 => flip wrt Y, -1 => flip both
flipped = cv.flip(img, -1)
cv.imshow('Flipped', flipped)

## CROPPING ##

# Just write which pixel you need
cropped = img[200:400, 100:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)