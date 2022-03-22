from cryptography.fernet import Fernet
from time import sleep
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
class BColors:

    BACKBLUE = '\033[44m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKBLUE = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033[0m'


class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dic = {}

    def createKey(self,path):
        self.key = Fernet.generate_key()
        print(self.key)
        with open(path, 'wb') as f:
            f.write(self.key)
            
    def loadKey(self,path):
        with open(path,'rb') as f:
            self.key = f.read()
        
    def createPassFile(self,path, initial_values = None):
        self.password_file = path
        # with open(path, 'w') as f:
        if initial_values is not None:
            for key, values in initial_values.items():
                self.addPassword(key,values)
            
    def loadPassFile(self, path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dic[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    
    def addPassword(self,site,password):
        self.password_dic[site]  = password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + str(encrypted.decode())+ "\n")
                
    def getPassword(self, site):
        return self.password_dic[site]
    
    
    
def main():
    password = {
        "PLACEHOLDER-PASS-1": "743z4782",
    }
    
    pm = PasswordManager()
    clearConsole()
    print(BColors.BOLD+BColors.OKCYAN+(r"""
 ______    __     _______  _______    _  _  _   __  _______  _______  __     ______   _____   
(_____ \  / /    (_______)(_______)  | || || | /  |(_______)(_______)/ /    (_____ \ (____ \  
 _____) )/ /____  ______   ______    | || || |/_/ |   __       __   / /____  _____) ) _   \ \ 
|  ____/|___   _)(_____ \ (_____ \   | ||_|| |  | |  / /      / /  |___   _)(_____ ( | |   | |
| |         | |   _____) ) _____) )  | |___| |  | | / /____  / /____   | |        | || |__/ / 
|_|         |_|  (______/ (______/    \______|  |_|(_______)(_______)  |_|        |_||_____/  

                                    Version 0.0.8
                               Copyright © 2022 S3R43o3
""")+BColors.CLEAR)
    print(BColors.ORANGE+BColors.BOLD+(f"""\n
        What do you want to do?
                                       
        (1) Create a new key
        (2) Load an existing key
        (3) Create new password file
        (4) Load existing password file
        (5) Add a new password
        (6) Get a password
        
        (q) Quit              
    """+BColors.CLEAR))
    done = False
    while not done:
        choice = input(BColors.BOLD+BColors.OKBLUE+"Enter a Option: "+BColors.CLEAR)
        if choice == "1":
            path = input(BColors.BOLD+BColors.OKBLUE+"Enter keyname: "+BColors.CLEAR)
            pm.createKey(path)
        elif choice == "2":            
            path = input(BColors.BOLD+BColors.OKBLUE+"Enter keyname to load: "+BColors.CLEAR)
            pm.loadKey(path)
        elif choice == "3":
            path = input(BColors.BOLD+BColors.OKBLUE+"Enter a name for new passwordfile: "+BColors.CLEAR)
            pm.createPassFile(path, password)
        elif choice == "4":
            path = input(BColors.BOLD+BColors.OKBLUE+"Enter the name of passwordfile to load: "+BColors.CLEAR)
            pm.loadPassFile(path)
        elif choice == "5":
            site = input(BColors.BOLD+BColors.OKBLUE+"Enter site: "+BColors.CLEAR)
            password = input(BColors.BOLD+BColors.OKBLUE+"Enter password: "+BColors.CLEAR)
            pm.addPassword(site,password)
        elif choice == "6":
            site = input(BColors.BOLD+BColors.OKBLUE+"What site password you want?: "+BColors.CLEAR)
            print(BColors.ORANGE+BColors.BOLD+f"Password for {site} is {pm.getPassword(site)} "+BColors.CLEAR)
        elif choice == "q":
            done = True
            print(BColors.RED+BColors.BOLD+"\n <<<<< Bye! >>>>>\n\n"+BColors.CLEAR)            
        else:
            print(BColors.BOLD+BColors.RED+'Invalid Option!\nPlease enter a valid Option!'+BColors.CLEAR)
            sleep(1.5)
            main()
    quit(0)

if __name__=='__main__':
    main()        







