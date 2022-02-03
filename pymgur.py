import json
import os
import platform
import random
import time
from os import path

import colorama
import pyimgur
import requests
from colorama import Back, Fore, Style
from imgur_python import Imgur

if platform.system == 'Linux' or 'MacOS':
    os.system('clear')
else:
    os.system('cls')


try:
    cid = open("clientid.txt","r")
    readcid = cid.read()
except FileNotFoundError:
    print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}Couldn't find clientid.txt file! Creating one for you...")
    time.sleep(1)
    fp = open('clientid.txt', 'x')
    fp.close()
    print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}clientid.txt Has been Created!")
    time.sleep(2)
    if platform.system == 'Linux' or 'MacOS':
        os.system('clear')
    else:
        os.system('cls')
        
rndm = random.randint(0,999999)

print(Fore.MAGENTA + f"""
   

██████╗░██╗░░░██╗███╗░░░███╗░██████╗░██╗░░░██╗██████╗░
██╔══██╗╚██╗░██╔╝████╗░████║██╔════╝░██║░░░██║██╔══██╗
██████╔╝░╚████╔╝░██╔████╔██║██║░░██╗░██║░░░██║██████╔╝
██╔═══╝░░░╚██╔╝░░██║╚██╔╝██║██║░░╚██╗██║░░░██║██╔══██╗
██║░░░░░░░░██║░░░██║░╚═╝░██║╚██████╔╝╚██████╔╝██║░░██║
╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝.py   

{Fore.RED}💕 Imgur Image/Video Uploader via Python
""")




if os.stat("clientid.txt").st_size == 0:

    
    time.sleep(1)
    def clientidsetup():
        print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}No client ID has been set. You cannot use Pymgur without providing Imgur Client ID")
        cidyes = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Setup Client ID now? (Y/n): ")
        if cidyes == 'Y' or cidyes == 'y' or cidyes == '':
            print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}Setting up Client ID...")
            time.sleep(1)
            print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}Create your Client ID here: https://api.imgur.com/oauth2/addclient")
            clientidprompt = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Enter your Imgur Client ID: ")
            if len(clientidprompt) <10 or len(clientidprompt) >16:
                print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}Invalid Client ID!")
                time.sleep(1)
                print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}Restarting Client ID Setup Proccess...")
                time.sleep(2)
                clientidsetup()
            else:
                f = open("clientid.txt", 'a')
                f.write(clientidprompt)
                print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}Client ID Saved! From now, you won't be asked to enter your client id again!")
                time.sleep(2)
                if platform.system == 'Linux' or 'MacOS':
                    os.system('clear')
                else:
                    os.system('cls')  
                print("Restart the script to apply changes...")
                time.sleep(2)
                exit()
                
                
        else:
            print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}Client ID was not set up! Aborting...")
            time.sleep(3)
            exit()
    clientidsetup()
            
        
try:
    time.sleep(1.1)
    CLIENT_ID = readcid
    PATH = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Path/URL to Image/Video: ")
    print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}Uploading...")

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title=f"Pymgur_{rndm}")
    print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}TITLE: " + uploaded_image.title)
    print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}LINK: " + uploaded_image.link)
    print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}TYPE: " + uploaded_image.type)
    print("")
    print(f"{Fore.WHITE}[{Fore.GREEN}OK{Fore.WHITE}] {Fore.MAGENTA}Uploaded!")
except LookupError:
    print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}No valid Path/URL was specified!")
    time.sleep(3)
    exit()
except FileNotFoundError:
    print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}This file doesn't exist!")
except:
    print(f"{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] {Fore.MAGENTA}An unknown error occured. You may not have set up auth.py")
