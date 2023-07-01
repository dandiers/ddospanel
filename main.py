#remake boleh tapi izin dulu!! 
#t.me/mrd4nd

import subprocess
import os
import time
import socket
import requests
import random
import getpass
import sys
import json
import platform
import colorama
from node_modules.colors.themes import string

#JANGAN DI UBAH DEK! #
#JANGAN DI UBAH DEK! #
author = "dandier"
#JANGAN DI UBAH EEK! #
#JANGAN DI UBAH DEK! #

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 0, 0)
end_color = (0, 0, 255)

class Color:
	colorama.init(autoreset=True)
	LB = colorama.Fore.LIGHTBLUE_EX
	LC = colorama.Fore.LIGHTCYAN_EX
	LG = colorama.Fore.LIGHTGREEN_EX
	LR = colorama.Fore.LIGHTRED_EX
	LY = colorama.Fore.LIGHTYELLOW_EX
	RESET = colorama.Fore.RESET
	
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = r"""
				▓████▄ ▓█████▄  ▒█████    ██████ 
				▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
				░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
				░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
				░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
				 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
				 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
				 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
				   ░       ░        ░ ░        ░  
				 ░       ░                       
"""
    author = r"""
					Ddos Panel By Dandier
    """
    prints(start_color, end_color, banner)
    prints(end_color, start_color, author)
    print("\n") 
    print(Color.LB+"                                  ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LY+" dandier"+Color.LR+"       ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" flood")
    print("\n") 
    print(Color.LR+"                                  ["+Color.LG+"VIP"+Color.LR+"]"+Color.LC+" gangbang"+Color.LB+"       ["+Color.LR+"VVIP"+Color.LB+"]"+Color.LY+" socket")
    print("\n")
    
    while True:
        cnc = input(Color.LB+"╔═══"+Color.LR+"["+Color.LG+"root"+Color.LB+"@"+Color.LG+"dandier"+Color.LR+"]"+Color.LB+"\n╚══> "+Color.RESET)
        if "gangbang" in cnc:
            try:
                gb = os.path.join("node_modules/randomstring", "input.py")
                subprocess.run(['python3', gb])
                sys.exit(0)
            except IndexError:
                print('just input gangbang')
        
        elif "dandier" in cnc:
            try:           
                dandier = os.path.join("node_modules/dashdash/etc", "input.py")
                subprocess.run(['python3', dandier])
                sys.exit(0)
            except IndexError:
                print('just input dandier')
                
        elif "flood" in cnc:
            try:
                flood = os.path.join("node_modules/aws4", "input.py")
                subprocess.run(['python3', flood])
                sys.exit(0)
            except IndexError:
                print('just input flood')
                
        elif "raw" in cnc:
            try:
                raw = os.path.join("node_modules/asn1/lib/ber", "input.py")
                subprocess.run(['python3', raw])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                
        elif "socket" in cnc:
            try:
                socket = os.path.join("node_modules/colors/lib/system", "input.py")
                subprocess.run(['python3', socket])
                sys.exit(0)
            except IndexError:
                print('just input raw')
                                
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Method: [ " + cmmnd + " ] Tidak Di Temukan!")
            except IndexError:
                pass
                
if author == "dandier":
    main()
else:
    string.authorsalah()