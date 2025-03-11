import cv2 as cv
import numpy as np

## Each image is made with three channels : Blue Green Red
# It's possible to split the immage in order to display only one channel.
# The resultant image is in a gray scale, that represent the distribution of the color' density:
# light => high density     dark => low density

img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

# Use the split function to get the three images
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
# Print the shape
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


## MERGE ##

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

## SHOW THE COLORS IN A MERGED IMAGE ##

blue = cv.merge([b,blank,blank])    # By putting blank in the green and red place, I only display the blue channel
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue Merged', blue)
cv.imshow('Green Merged', green)
cv.imshow('Red Merged', red)



cv.waitKey(0)