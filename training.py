import cv2
import numpy as np

#creating Fisherface Recognizer
face_rec = cv2.face.FisherFaceRecognizer_create(29)

#creating read csv function
def read_csv(file1):
    (faces, labels) = ([],[])
    fp = open(file1, 'r')
    lines = fp.readlines()
    for line in lines:
        new = line.strip()
        face, label = new.split(';')
        #detecting faces
        check = cv2.imread(face)
        detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        detects = detect.detectMultiScale(check)
        for (w,x,y,z) in detects:
            #creating the rectangle
            cv2.rectangle(check, (w,x), (w+y, x+z), (255,255,255), 2)
            newflip = check[w:w+y, x:x+z]
            #checking if a face is detected, if so then add to arrays
            if(len(check[w:w+y, x:x+z]) != 0):
                #trainer needs to be trained with grayscale photos
                gray = cv2.cvtColor(check[w:w+y, x:x+z], cv2.COLOR_BGR2GRAY)
                #converting all images to sam size
                gray = cv2.resize(check[w:w+y, x:x+z], (150,150))
                faces.append(gray)
                labels.append(np.array(int(label)))
            
    #print(type(faces))
    faces = np.asarray(faces)
    labels = np.asarray(labels)
            
    return faces, labels


#getting faces and labels from data file            
faces, labels = read_csv('data.csv')

#training model
face_rec.train(faces, labels)
face_rec.write('trained_rec.yml')


