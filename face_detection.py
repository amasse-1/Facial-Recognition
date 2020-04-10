import Tkinter as tk #to create the GUI
from PIL import ImageTk, Image #to put the stream in the GUI
import cv2 #for computer vision
import email_alert as ea
import os
import time

root = tk.Tk()
root.title('Raspberry Pi Camera')

frame = tk.Frame(root, bg="white")
frame.grid()

label = tk.Label()
label.grid()

root.grid_rowconfigure(20, weight=1)
root.grid_columnconfigure(20, weight=1)

#camera
cam = cv2.VideoCapture(0)

#framerate = 60fps
cam.set(cv2.CAP_PROP_FPS, 60)

#haar-cascade default
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#video stream function
def stream():
    _, frame = cam.read()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    flip = cv2.flip(im, 1) #flips the camera horizontally
    x = faceDetect(flip)
    if x == True:
        takePic(frame)
        x = False
    img = Image.fromarray(flip)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    #delay to increase proficiency and to try to reduce CPU temp
    label.after(2, stream)

#function to take new photo of the
def takePic(img):
    newImg = "Detected_Intruder.png"
    #saves image
    cv2.imwrite(newImg,img)
    #creates image and sends alert
    ea.send_alert(pic=newImg)
    #deletes the image to save memory
    os.remove(newImg)
    #10 second wait to delay the amount of emails sent
    time.sleep(10)

#face detection
def faceDetect(ex):
    boolean = False
    detects = face_xml.detectMultiScale(ex, 1.1, 3)
    for (w,x,y,z) in detects:
        #creating the rectangle
        cv2.rectangle(ex, (w,x), (w+y, x+z), (255,255,255), 4)
        newflip = ex[x:x+z, w:w+y]
        new_size = cv2.resize(ex[x:x+z, w:w+y], (150,150))
        num, name = face_rec(new_size)
        #if there is a trusted face display their faces
        if(num != -1):
            cv2.putText(ex, name, (w, x), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,255), 2)
        #if there is an intruder return a boolean to the send_alert function
        if(num == -1):
            boolean = True
            return boolean
        return boolean
    return boolean
            
def face_rec(ex):
    #face recognizer
    rec = cv2.face.FisherFaceRecognizer_create()
    x = rec.read('trained_rec.yml')
    
    #needs to be grayscale to predict
    ex = cv2.cvtColor(ex, cv2.COLOR_BGR2GRAY)
    
    #predict function to give the person's number and confidence level
    num, conf = rec.predict(ex)
    
    #getting the name of the person
    name = rec.getLabelInfo(num)
    
    return num, name

#start button to begin the stream
start = tk.Button(root, text="Start Stream", command= lambda: stream())
start.grid()

#stop button to close the program
stop = tk.Button(root, text="Stop Stream", command=root.destroy)
stop.grid()

root.mainloop()
