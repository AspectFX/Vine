#Modules
import os

menu = input("""
             

____   ____.__               
\   \ /   /|__| ____   ____  
 \   Y   / |  |/    \_/ __ \ 
  \     /  |  |   |  \  ___/ 
   \___/   |__|___|  /\___  >
                   \/     \/ 
             
                     
[1] Timeout - DDOS Tool

[2] Remote C4 - E-Mail Bomber

[3] Brute - Website Password Cracker

[4] AdbSploit - ADB Hacking Tool (Setup)

[5] AdbSploit - ADB Hacking Tool
 
[6] WifiKit - Wiki Hacking Toolbox

[7] XCTR - Hacking Tool Swept

[8] Quit
             
             """)

if menu == '1':
    os.system('clear')
    os.system('python3 Timeout.py')
    
if menu == '2':
    os.system('clear')
    os.system('python3 RemoteC4.py')
    
if menu == '3':
    os.system('clear')
    os.system('python3 brute.py')
    
if menu == '4':
    os.system('clear')
    os.chdir('extra/adbsploit')
    os.system('sudo python3 setup.py install')
    
if menu == '5':
    os.system('clear')
    os.chdir('extra/adbsploit/adbsploit')
    os.system('sudo python3 adbsploit.py')
    
if menu == '6':
    os.system('clear')
    os.chdir('extra/Wifi-Hacking/')
    os.system('sudo python3 Wifi-Hacking.py')
    
if menu == '7':
    os.system('clear')
    os.chdir('extra/XCTR-Hacking-Tools/')
    os.system('pip3 install -r requirements.txt')
    os.system('python3 xctr.py')
    
if menu == '8':
    quit()
