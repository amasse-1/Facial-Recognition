import cv2
import numpy as np
import os 

#creating Fisherface Recognizer
face_rec = cv2.face.FisherFaceRecognizer_create()

def read_csv(file1):
    faces = []
    faceArray = []

    csv = open(file1)
    lines = csv.readlines()
    
    for line in lines:
        faces.append(line.strip())
        for face in faces:
            #reading images
            new = cv2.imread(face)
            #creating gray scale images
            gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
            faceArray.append(gray)
            return faceArray

faces = read_csv('data.csv')
names = ['Anthony', 'Jalen', 'Kaylee']
face_rec.train(src=faces, labels=names)

        
