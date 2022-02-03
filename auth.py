import webbrowser
import pyimgur
import time
import colorama
import os
import platform

from colorama import Fore


if platform.system == 'Linux' or 'MacOS':
    os.system('clear')
else:
    os.system('cls')
print("""
 
 
      
""")
print(f"{Fore.WHITE}[{Fore.CYAN}INFO{Fore.WHITE}] {Fore.MAGENTA}You HAVE to set this up correctly! If you won't, you will not be able to use this script!")
time.sleep(3)


print("""
      

░█████╗░██╗░░░██╗████████╗██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██║░░██║
███████║██║░░░██║░░░██║░░░███████║
██╔══██║██║░░░██║░░░██║░░░██╔══██║
██║░░██║╚██████╔╝░░░██║░░░██║░░██║
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝.py      

      """)

print("\nGet your Client ID & Secret here: \nhttps://api.imgur.com/oauth2/addclient \n")
CLIENT_ID = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Client ID: ")
CLIENT_SECRET = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Client Secret: ")


im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)
auth_url = im.authorization_url('pin')
webbrowser.open(auth_url)
pin = input(f"{Fore.WHITE}[{Fore.GREEN}???{Fore.WHITE}] {Fore.MAGENTA}Paste the PIN: ")
im.exchange_pin(pin)
im.create_album("Pymgur", "Pymgur Album for all Images/Videos uploaded via Pymgur!")
im.refresh_access_token()