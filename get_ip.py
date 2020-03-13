#!/usr/bin/python3

"""

author: @endormi

"""

from email.message import EmailMessage
from pathlib import Path
from pyfiglet import figlet_format
from termcolor import cprint
import platform
import requests
import smtplib
import socket
import time


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


logo = 'IP Address && System'

info = color.NOTICE + '''
Hello,
This is an IP Address and System getter (not that useful).
What does it do? It adds the computer IP Address & System information to a log.txt file.
When the limit is reached (current limit is 40), it sends the file to the given email and starts over by overwriting log.txt.\n''' + color.END

r = requests.get('https://api.ipify.org')

host = socket.gethostname()
addr = r.text
__sys__ = platform.system()
__rel__ = platform.release()
__v__ = platform.version()
__m__ = platform.machine()

file = Path('log.txt')


while True:
    if file.is_file():
        lines = open(file, 'r').readlines()
        break

    else:
        Path('log.txt').touch()


def ap():
    with open(file, 'a') as i:
        i.write('Computer name: ' + host + '\n')
        i.write('IP Address: ' + addr + '\n')
        i.write('Your system: ' + __sys__ + ' ' + 'Version: ' + __v__ + ' ' + 'Machine: ' + __m__ + ' ' + 'Release: ' + __rel__ + '\n')
        i.write('\n')


if len(lines) == 40:  # increase when needed
    cprint(figlet_format(logo, font='slant'), 'green')

    PORT = 587  # Gmail

    email = 'example@company.com'
    # Get your password: https://myaccount.google.com/apppasswords
    password = 'example_password'

    with smtplib.SMTP('smtp.gmail.com', PORT) as send__mail:
        send__mail.starttls()
        send__mail.login(email, password)

        message = EmailMessage()
        message['From'] = email
        message['To'] = email
        message['subject'] = 'IP Address & System'
        message.set_content('Here is the file')
        message.add_attachment(open('log.txt', 'r').read(), filename='log.txt')

        send__mail.send_message(message)

        print('Limit reached!')
        print(f'Current limit is: {len(lines)}.\n')
        time.sleep(1)
        print('Sending Email...')
        time.sleep(1)
        print('Sent!\n')
        time.sleep(1)

    with open('log.txt', 'w') as f:
        f.write('Computer name: ' + host + '\n')
        f.write('IP Address: ' + addr + '\n')
        f.write('Your system: ' + __sys__ + ' ' + 'Version: ' + __v__ + ' ' + 'Machine: ' + __m__ + ' ' + 'Release: ' + __rel__ + '\n')
        f.write('\n')
        print('Overwriting the file...')
        time.sleep(1)
        print('Done!')

# First-time running
elif len(lines) == 0:
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info)
    ap()
    print('Creating a log.txt file...')
    time.sleep(1)
    print('Done!\n')
    time.sleep(1)
    print('Adding the first result...')
    time.sleep(1)
    print('Done!')

else:
    ap()
    print(f'Current length of the file: {len(lines)}.\n')
    print('Appending to ' + 'log.txt...')
    time.sleep(1)
    print('Done!')
