import time
from rubika import Bot
from pyfiglet import Figlet
from os import system
import platform
from data import *

bot = Bot('APP', auth, privateKey=key)

def cls():
    if platform.uname().system.lower() == "windows":
        system("cls")
    else:
        system("clear")

cls()

f = Figlet(font='slant')
print(f.renderText('Bot Rubika'))

id = str(input('Enter the user id: ')).replace("@", "")
sms = str(input('Enter the message: '))
range_count = int(input('Enter the range: '))

try:
    response = bot.getInfoByUsername(id)
    guidtarget = response['data']['user']['user_guid']
    print("User GUID:", guidtarget)
except KeyError:
    print("Error: Invalid username or unable to retrieve user info.")
    exit(1)

for i in range(range_count):
    try:
        result = bot.sendMessage(guidtarget, sms)
        if result.get('data'):
            print(f'Message {i+1} sent to {id}')
        else:
            print(f'Failed to send message {i+1} to {id}')
    except Exception as e:
        print(f"Error while sending message: {e}")
    time.sleep(0.2)