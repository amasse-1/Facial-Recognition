import cv2
import numpy as np

#creating Fisherface Recognizer
face_rec = cv2.face.FisherFaceRecognizer_create(30, 750.0)

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
            rect = cv2.rectangle(check, (w,x), (w+y, x+z), (255,255,255), 2)
            newflip = check[x:x+z, w:w+y]
            #checking if a face is detected, if so then add to arrays
            if(len(check[x:x+z, w:w+y]) != 0):
                #trainer needs to be trained with grayscale photos
                gray = cv2.cvtColor(check[x:x+z, w:w+y], cv2.COLOR_BGR2GRAY)
                #converting all images to sam size
                gray = cv2.resize(gray, (150,150))
                #appending image and labels to 
                faces.append(np.array(gray))
                labels.append(np.array(int(label)))
            
    #changing data types to numpy arrays
    faces = np.array(faces)
    labels = np.array(labels)
            
    return faces, labels

#getting faces and labels from data file            
faces, labels = read_csv('data.csv')

#Adding labels for the names
face_rec.setLabelInfo(0, 'Anthony')
face_rec.setLabelInfo(1, 'Jalen')
face_rec.setLabelInfo(2, 'Kaylee')

#training model
face_rec.train(faces, labels)
#save model to be used in different functions
face_rec.write('trained_rec.yml')
