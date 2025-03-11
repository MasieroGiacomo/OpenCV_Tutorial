import cv2 as cv

## READ IMAGES ##

# Take a path to an image and return that image as a matrix of pixels
img = cv.imread('Images/FaticaNeiMateriali.png') 
# Display image in a new window.  'name of the window', whatToDisplay
cv.imshow('Test', img)  
# Wait for infinite time for a key to be pressed. more in the future
cv.waitKey(0)   


## READ VIDEOS ##

# Put an int to read your camera (0,1...) or the path of the file
capture = cv.VideoCapture(0)
capture = cv.VideoCapture('Videos/Coibentazione.mp4')
# Read the video frame by frame with a while loop, capture.read() returns the frame and a boolean for success of the op
while True:
    isTrue, frame = capture.read()
    # Display each frame of the video
    cv.imshow('Test', frame)
# To stop the video, if I press D key
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
# Release the capture device and destroy all windows 
capture.release()
cv.destroyAllWindows() 


