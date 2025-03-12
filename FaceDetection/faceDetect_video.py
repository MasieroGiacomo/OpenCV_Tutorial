import cv2 as cv

capture = cv.VideoCapture(0)
capture = cv.VideoCapture('Videos/st3pny.gif')

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()

    # This is just to replay the gif without closing the program
    if not isTrue:  
        capture = cv.VideoCapture('Videos/st3pny.gif')
        continue 
    
    cv.imshow('Test', frame)
    
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in faces_rect:
        # Draw the rectangles onto the frames and display them
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=1)
        cv.imshow('Detected Faces', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 