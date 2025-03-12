import cv2 as cv

# The classifier looks to an object in a image and uses the edges to decide whether or not it's a face
# HaarCascade is very sensible to noise in the image, but they're more popular and easy to use

img = cv.imread('Images/people.jpeg')
cv.imshow('People', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Create an haar variable, read all the lines of haar_face.xml and save them in
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Return the rectangular coordinates of the face as a list into the variable
# (source image, scaleFactor, minimumNeighbors)
# By increasing minNeighbors it's possible to reduce noise, but it could not detect faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# Print how many faces were found
print(f'Number of faces found: {len(faces_rect)}')

# Draw a rectangle over the faces that have been found (x,y)=coordinates of top right, (w,h)=width,height
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)