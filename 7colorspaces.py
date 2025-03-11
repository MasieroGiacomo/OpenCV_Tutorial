import cv2 as cv

## OpenCV sees images as BGR (Blue-Green-Red)
# Can also do the conversion back (ex: gray->bgr)
# ! CAN'T do direct conversion between spaces (ex: gray->HSV), ALWAYS need to pass through BGR !


img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)

## BGR TO GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # cv.COLOR_HSV2BGR to go back
cv.imshow('Gray Scale', gray)

## BGR TO HSV (Hue->type of color in a color wheel, Saturation->purity of the color(0-100%), Value->brightness(0=black, 100=white))
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Space', hsv)

## BGR TO LAB (Lightness->brightness, A->green to red color spectrum, B->blue to yellow color spectrum)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB Space', lab)

## BGR TO RGB (Red Green Blue)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Space', rgb)



cv.waitKey(0)