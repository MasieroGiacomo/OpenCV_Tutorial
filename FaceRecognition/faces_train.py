import cv2 as cv
import numpy as np
import os

people = []
# Use this to write the directories into a list
for i in os.listdir(r'C:/Personale/Universita/Tongji/OpenCV/OpenCV_Tutorial/FaceRecognition/Dataset'):
    people.append(i)  
print(people)

DIR = r'C:/Personale/Universita/Tongji/OpenCV/OpenCV_Tutorial/FaceRecognition/Dataset'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Function that loops over all the dataset and over all the pictures inside them, and grab the features of the faces
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        if not os.path.isdir(path):  # Controlla se è una cartella, altrimenti salta
            continue  

        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            if img_array is None:  # Controllo se l'immagine è valida
                continue  

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print('-- Training done --')
# Debug to see if it works
#print(f'The lenght of the features is: {len(features)}')
#print(f'The lenght of the labels is: {len(labels)}')

 ## FACE RECOGNIZER ##

features = np.array(features, dtype='object')
labels = np.array(labels, )

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the lists that were made
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)



