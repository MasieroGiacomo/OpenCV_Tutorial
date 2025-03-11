import cv2 as cv

## FUNCTION TO RESCALE ##

# Input: frame itself, default scale.       ! Works for images, videos and live videos !
def rescaleFrame(frame, scale = 0.3):
    # Scale width and height of the frame       ! Transform new values from float to int !
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # Save the new dimensions
    dimensions = (width, height)

    # Return the resized frame, using the interpolation mehod INTER_AREA (good when downsampling)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
## FUNCTION TO CHANGE RESOLUTION ##

# Input: desired width and height.      ! Works only on live feeds !
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


## RESCALE AN IMAGE ##

img = cv.imread('Images/FaticaNeiMateriali.png') 

# Resize the image
img_res = rescaleFrame(img)
# Show the image
cv.imshow('Test Resized', img_res)
cv.imshow('Test', img)  

cv.waitKey(0)  


## RESCALE A VIDEO ##

capture = cv.VideoCapture(0)
#capture = cv.VideoCapture('Videos/Coibentazione.mp4')

# To change the resolution of live feed
#changeRes(1920, 1080)

while True:
    isTrue, frame = capture.read()

    # Resize the frame and show it
    frame_res = rescaleFrame(frame)
    cv.imshow('TestResized', frame_res)

    cv.imshow('Test', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 