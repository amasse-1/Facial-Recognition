import os
from smtplib import SMTP
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi
from email.mime.multipart import MIMEMultipart as mm

#function to send the email notification
def send_alert(pic):
    #reads the image
    img = open(pic, 'rb').read()
    #creates the to, from, and subject
    msg = mm()
    msg['Subject'] = 'Intruder in Your Space'
    msg['From'] = 'csc521.facerec@gmail.com'
    msg['To'] = 'anthonyjmasse@gmail.com'
    
    #gets the text and image of the person.
    text = mt('Intruder! There is an intruder in your space! Here is a photo of them!')
    msg.attach(text)
    attach = mi(img, name=os.path.basename(pic))
    msg.attach(attach)

    #using the gmail server to send the email
    email = SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.ehlo()
    email.login('csc521.facerec@gmail.com', '######')
    email.sendmail('anthonyjmasse@gmail.com', 'anthonyjmasse@gmail.com', msg.as_string())
    email.quit()
