import cv2

#creating Fisherface Recognizer
face_rec = cv2.face.FisherFaceRecognizer_create(15)

if face_rec.empty():
    print('Empty data set')
