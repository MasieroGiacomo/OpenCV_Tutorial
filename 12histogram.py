import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

## Histograms help visualize the distribution of pixel intensity in an image (both gray/RGB images)

img = cv.imread('Images/desktop.jpg')
cv.imshow('Fatica', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

## 1. HISTOGRAM FOR GRAY SCALE ##
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat', gray)

# ([image], [channels to be utilized. 0 cause it's gray], mask (none),
#   histSize(# of bins, or columns of the histogram), [range](# of bits to be considered))
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# USE OF A MASK
'''
#circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#mask = cv.bitwise_and(gray, gray, mask=circle)
#gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
'''
# Use matplotlib to plot the histogram
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
'''


## 2. COLOR HISTOGRAM ##
'''
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

# Create a tuple for the three color channels
colors = ('b', 'r', 'g')
# Plot an histogram for each color
for i,col in enumerate(colors):
    # ([image], [channel], mask, [bins], [range])
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
'''
# USE OF A MASK
'''
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 300, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

colors = ('b', 'r', 'g')
for i,col in enumerate(colors):
    # ([image], [channel], mask, [bins], [range])
    hist = cv.calcHist([masked], [i], mask, [256], [0,256])     # ! mask ! 
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
'''


cv.waitKey(0)