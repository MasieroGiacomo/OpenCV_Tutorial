import cv2 as cv

## Images tend to have noise caused by camera sensors or bad lighting. It's possible to reduce this noise
# by applying some blurring methods
# A kernel window is defined over a specific part of the image. In practice, the kernel window is a grid with odd rows and columns
#   that cover a specific area of an image


img = cv.imread('Images/Cat.jpeg')
cv.imshow('Cat', img)

## 1. AVERAGING ##
# The intensity of the pixel of the central region of the kernel becomes the average of all the regions that surround it
#   the window slides over all the image from top left to bottom right

average = cv.blur(img, (3,3))       # Higher the size of the kernel, more the blur
cv.imshow('Average Blur', average) 

## 2. GAUSSIAN BLUR ##
# As average, but each surrounding pixel is given a particular weight, and the average of the product of these weights is
#   the new value of the central pixel
# ! Less blur than average, but looks more natural !

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)


## 3. MEDIAN BLUR ##
# As average, but instead of averaging it founds the median of the surrounding pixels
# ! Tends to be more effective in noise reduction than the others, most use in computer vision !

median = cv.medianBlur(img, 3)          # The kernel can just be an integer
cv.imshow('Median Blur', median)


## 4. BILATERAL BLUR ##
# The most effective way
# With respect to the other methods, it blurs the image but also retain the edges

# source, diameter of the pixel neighborhood, color standard deviation(higher value allows more colors to be considered when averaging pixels),
#    spatial standard deviation ( larger value allows farther pixels to influence the filtering process)
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
