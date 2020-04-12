# CSC-520-521: Facial Recongition Security Camera using Raspberry Pi
This Capstone Project uses facial detection, facial recognition, and email notification within a security camera using a Raspberry Pi
________
# Tools:

## Software: 
### Language and Version:
* **Python 2.7** 

 **_note:_** *can be used with Python 3.x, there just needs to be some small changes to allow the program to work correctly*

### For email notification:
* **smtplib** - a Python Library which helps with sending emails from a Python program. 
* **email.mime** - another Python library which helps with emails and Multipurpose Internet Mail Extensions (MIME), which is useful for attaching images to emails.
    
### For Facial detection and recognition: 
* **OpenCV** - an open source computer vision library with the following algorithms used:
   * **Haar-Cascades:** a facial detection algorithm in the algorithm uses black and white squares in different length and widths to help        locate a face within an image or video stream. These black and white squares are classifiers which calculate the number of pixels        under both colors and subtract the sum of pixels under the white from the sum of pixels under the black. These classifiers help          detect the faces within the photo.  
   * **Fisherface:** a facial recongition algorithm which increases visibility of main facial features within an image from the data set          such as: nose, bridge, mouth, eyes; while blurring the other features within that image. Then, after this process is done, the          algorithm will use the new trained model to determine the identity of an individual in the video frame. 

### Other tools:
* **os** - a Python library used specifically to delete unnecessary images to free up memory for this project. 
* **Tkinter** - used to create the GUI
* **Pillow (PIL)** - Python Imaging Library, this library is used to create the video stream to the GUI 

## Hardware:
* **Raspberry Pi 3 Model B+**
* **Raspberry Pi CPU Fan** 
* **ELP 2.1mm Wide Angle 5 Megapixel Camera**

## Email Notifications
One huge feature of this program is to use email notification to notify the primary user of individuals that are not allowed within the space in which the camera is placed. The notifications will include a photo of the intruder which is sent via email from the designated email address for this project which is: csc521.facerec@gmail.com. 

## Facial Detection 
This project uses Haar-Cascades to find faces within the video stream coming from the camera. The face detection finds the face and then from that point takes the face of that individual, focuses in on the face, resizes the face to be the same size as the faces within the data set, and then runs it through the recognizer. 

## Facial Recognition
The recongizer uses the Fisher Face algorithm to determine how close the individual matches with any of the individuals within the data set. The Fisher Face algorithm uses the photos from the data set and changes those photos to focus on certain parts of the face such as: eyes, nose, the bridge, etc. This makes it easier for the algorithm to determine if this new photo of a specific person is within the recognizable individuals or if it is an intruder. If the individual is recongnized then there won't be an email notification. However, if the individual is not recognized then there will be an email sent to thr primary user to then take it from there. 
