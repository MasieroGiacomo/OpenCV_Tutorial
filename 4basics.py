import cv2 as cv

img = cv.imread('Images/FaticaNeiMateriali.png')
cv.imshow('OG', img)

## TURN AN IMAGE INTO GRAY SCALE ##

# (image to transform, code of the op)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', gray)

## BLUR AN IMAGE ##

# (image to transform, (kernel size), other thing)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)       # Higher the kernel size, blurer the image
cv.imshow('Blurred Image', blur)

## DRAW EDGES ##

# (source image, threshold1, threshold2)    ! thre1 => if pixel value < th1 => put to black, if pixel > th2 => put to white
canny = cv.Canny(img, 125, 175)                 # If I give blur, less edges are found
cv.imshow('Edges', canny)

## DILATING AN IMAGE ##

# (source image, (kernel size), iterations)
dilated = cv.dilate(canny, (7,7), iterations=3) # Based on iteration, the image dilate more
cv.imshow('Dilated', dilated)

##  ERODE AN IMAGE ##

# (source image, (kernel size), iterations)
eroded = cv.erode(dilated, (3,3), iterations=3)     # ! If i put same kernel, iteration as in dilate, I obtain the og image
cv.imshow('Eroded', eroded)

## RESIZE AN IMAGE ##

# (source, (new dimensions), interpolation)         ! DOES NOT CARE ABOUT THE ASPECT RATIO !
resized = cv.resize(img, (500,500))     # interpolation=cv.INTER_AREA when shrinking, INTER_LINEAR / INTER_CUBIC when enlarge
cv.imshow('Resized', resized)

## CROPPING AN IMAGE ##

# source image[which pixel to take]
cropped = img[50:200, 100:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)  