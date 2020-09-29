import requests
import os
from dhooks import Webhook, Embed
print('''            _                          _     _                 _    
           (_)                        | |   | |               | |   
  __ _  ___ _  ___ _ __  __      _____| |__ | |__   ___   ___ | | __
 / _` |/ __| |/ _ \ '__| \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
| (_| | (__| |  __/ |     \ V  V /  __/ |_) | | | | (_) | (_) |   < 
 \__,_|\___|_|\___|_|      \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_''')
print('\n[1] Spam a single message\n[2] Spam several different messages')
option = input('\nOption: ')
cls = lambda: os.system('cls')
cls()

if "1" in option: 
    print('NOTE: Webhooks have to be in a discord.com/ format not a discordapp.com/ format\n\n')
    wh = input('Webhook Url: ')
    hook = Webhook(str(wh))
    message = input('Message to send: ')
    check = 1
    while True:
        try:
            hook.send(f'{str(message)}')
            check += 1
            print(f'Successfully sent a webhook. Total: {check}')
        except Exception as e:
            print(f'Error. Hook is likely invalid {e}')
if "2" in option:
    print('NOTE: Webhooks have to be in a discord.com/ format not a discordapp.com/ format\n\n')
    wh = input('Webhook Url: ')
    hook = Webhook(str(wh))
    msgcount = input('Amount of messages to send: ')
    msgstosend = []
    check = 1
    for i in range(int(msgcount)):
        message = input('Message to send: ')
        msgstosend.append(message)
    while True:
        for i in msgstosend:
            try:
                hook.send(f'{str(i)}')
                check += 1
                print(f'Successfully sent a webhook. Total: {check}')
            except Exception as e:
                print(f'Error. Hook is likely invalid {e}')
