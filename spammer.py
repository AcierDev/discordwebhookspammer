import requests
import os
from dhooks import Webhook, Embed
print('''            _                          _     _                 _    
           (_)                        | |   | |               | |   
  __ _  ___ _  ___ _ __  __      _____| |__ | |__   ___   ___ | | __
 / _` |/ __| |/ _ \ '__| \ \ /\ / / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
| (_| | (__| |  __/ |     \ V  V /  __/ |_) | | | | (_) | (_) |   < 
 \__,_|\___|_|\___|_|      \_/\_/ \___|_.__/|_| |_|\___/ \___/|_|\_''')
print('\n[1] Spam a single message\n[2] Spam several different messages\n[3] Nigeria spam\n[4] Gore spam\n[5] Porn spam')
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
if "3" in option:
    nigeriaphrases = [
        "@everyone praise nigeria! allah is god nigeria yes https://media.tenor.com/images/540dcfe1b85dc494915f94e3991eafdc/tenor.gif",
        "@everyone nigeria on top https://thumbs.gfycat.com/TanPleasedIberianmidwifetoad-small.gif",
        "@everyone nigeria is love. nigeria is life !!1111 https://www.gifservice.fr/img/gif-vignette-small/4347a0e1ea15d38d053a6448dd2e8c72/81310-flags-africa-nigeria-coeur.gif",
        "@everyone nigeria tbh https://thumbs.gfycat.com/LikelySereneIguanodon-size_restricted.gif",
        "@everyone nigeria was here https://i.gifer.com/Nf9Q.gif",
    ]
    print('NOTE: Webhooks have to be in a discord.com/ format not a discordapp.com/ format\n\n')
    wh = input('Webhook Url: ')
    hook = Webhook(str(wh))
    check = 1
    while True:
        for i in nigeriaphrases:
            try:
                hook.send(f'{str(i)}')
                check += 1
                print(f'Successfully sent a webhook. Total: {check}')
            except Exception as e:
                print(f'Error. Hook is likely invalid {e}')
