import os
from smtplib import SMTP
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi
from email.mime.multipart import MIMEMultipart as mm

def send_alert(pic):
    img = open(pic, 'rb').read()
    msg = mm()
    msg['Subject'] = 'Intruder in Your Space'
    msg['From'] = 'csc521.facerec@gmail.com'
    msg['To'] = 'anthonyjmasse@gmail.com'

    text = mt("Intruder! There is an intruder in your space! Here is a photo of them! ")
    msg.attach(text)
    attach = mi(img, name=os.path.basename(pic))
    msg.attach(attach)

    email = SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.ehlo()
    email.login('csc521.facerec@gmail.com', '#####')
    email.sendmail('anthonyjmasse@gmail.com', 'anthonyjmasse@gmail.com', msg.as_string())
    email.quit()
