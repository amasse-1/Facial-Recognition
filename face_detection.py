import tkinter as tk #to create the GUI
from PIL import ImageTk, Image #to put the stream in the GUI
import cv2 #for computer vision
import email_alert as ea

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
    faceDetect(flip)
    img = Image.fromarray(flip)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    #delay to increase proficiency and to try to
    #reduce CPU temp
    label.after(2, stream)

#check to see if a face is detected
face_det = False

if face_det == True:
	ea.send_alert()

#face detecttion
def faceDetect(ex):
    detects = face_xml.detectMultiScale(ex, 1.1, 3)
    for (w,x,y,z) in detects:
        #creating the rectangle
        cv2.rectangle(ex, (w,x), (w+y, x+z), (255,255,255), 2)
        newflip = ex[w:w+y, x:x+z]
        #sending notification
        face_det=True

#start button to begin the stream
start = tk.Button(root, text="Start Stream", command= lambda: stream())
start.grid()

#stop button to close the program
stop = tk.Button(root, text="Stop Stream", command=root.destroy)
stop.grid()

root.mainloop()
