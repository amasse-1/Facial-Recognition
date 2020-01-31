import os
from smtplib import SMTP
from email.mime.text import MIMEText as mt
from email.mime.image import MIMEImage as mi
from email.mime.multipart import MIMEMultipart as mm

def set_prim_user():
    print('Please enter primary user email and name')
    prim_user_email = input('Email: ')
    prim_user_name = input('Name: ')
    send_alert('#example photo path here',
            prim_user_email, prim_user_name)

def send_alert(pic, em, na):
    img = open(pic, 'rb').read()
    msg = mm()
    msg['Subject'] = 'Intruder in Your Space'
    msg['From'] = 'anthonyjmasse@gmail.com'
    msg['To'] = em

    text = mt("""Intruder! There is an intruder in your space! Here is a photo of them! """)
    msg.attach(text)
    attach = mi(img, name=os.path.basename(pic))
    msg.attach(attach)

    email = SMTP('smtp.gmail.com', 587)
    email.starttls()
    email.ehlo()
    email.login('csc521.facerec@gmail.com', '#Password here##')
    email.sendmail('anthonyjmasse@gmail.com', em, msg.as_string())
    email.quit()

set_prim_user()
