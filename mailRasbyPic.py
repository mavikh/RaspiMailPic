# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:21:19 2019

@author: Vima
"""
#Here we take a picture using camera module on Raspberry Pi
#and send it to an email
#To see the From and To mails on the email, they should be written
#as object like msg['from'] and msg['to']
from picamera import PiCamera
from time import sleep
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#from email.mime.text import MIMEText

#Take picture with camera module on raspberry-pi
camera = PiCamera()
camera.start_preview()
sleep(5)
picture = camera.capture('/home/pi/Pictures/pythonTest.jpg')
camera.stop_preview()

#Attach and send it to email
msg = MIMEMultipart()
msg.attach(MIMEImage(open('pythonTest.jpg', 'rb').read()))

fromMail = 'miscellaneous.obj@gmail.com'
#password = getpass.getpass()
password= 'mahboobeh11'
toMail = 'miscellaneous.obj@gmail.com'
msg['subject'] = 'Picture from Raspberry Pi!'
#subject = 'Picture from Raspberry Pi!'

try:
    server = smtplib.SMTP('smtp.gmail.com:587') #connect to gmail server
    server.starttls()
    server.login(fromMail, password)
    server.sendmail(fromMail, toMail, msg.as_string())
except Exception as e:
    print(e)     
finally:    
    server.quit()

