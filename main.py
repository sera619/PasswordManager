from cryptography.fernet import Fernet
from time import sleep
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
class BColors:
	OKGREEN= '\033[92m'
	BACKBLUE = '\033[44m'
	OKCYAN = '\033[96m'
	VIOLETT = '\033[95m'
	OKBLUE = '\033[34m'
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

		self.fistRun = True
		self.keySelected = False
		self.pathKey = None
		self.pathSelected = False
		self.pathFile = None
		


	def createKey(self,path):
		self.key = Fernet.generate_key()
		path ='data/keys/'+path+'.key'		
		with open(path, 'wb') as f:
			f.write(self.key)
			f.close()
		print(BColors.OKGREEN+'Success! New Passwordkey created\n'+BColors.CLEAR)
			
	def loadKey(self,path):
		self.pathKey = path
		path ='data/keys/'+path+'.key'
		if not os.path.exists(path):
			self.errMsg()
			sleep(2)
			return main()
		with open(path,'rb') as f:
			self.key = f.read()
			self.keySelected = True
			f.close()
		
	def createPassFile(self,path, initial_values = None):
  		# with open(path, 'w') as f:
		path ='data/files/'+path+'.pass'
		self.password_file = path
		if initial_values is not None:
			for key, values in initial_values.items():
				self.addPassword(key,values)
		print(BColors.OKGREEN+'Success! New Passwordfile created\n'+BColors.CLEAR)
			
	def loadPassFile(self, path):
		self.pathFile = path
		path ='data/files/'+path+'.pass'
		self.password_file = path
		if not os.path.exists(path):
			self.errMsg()
			sleep(2)
			return main()
		with open(path, 'r') as f:
			for line in f:
				site, encrypted = line.split(":")
				self.password_dic[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
			self.pathSelected = True
			f.close()
   
	def addPassword(self,site,password):
		self.password_dic[site]  = password
		if self.password_file is not None:
			with open(self.password_file, 'a+') as f:
				encrypted = Fernet(self.key).encrypt(password.encode())
				f.write(site + ":" + str(encrypted.decode())+ "\n")
				print(BColors.OKGREEN+"Success! New password saved!\n")
				f.close()

	def getPassword(self, site):
		if site is not self.password_dic:
			self.errMsg()
			sleep(2)
			return main()
		return self.password_dic[site]
	
	def errMsg(self):
		print(BColors.BOLD+BColors.RED+'>>>>>>>>> Invalid Option! Please enter a valid Option! <<<<<<<<<<'+BColors.CLEAR)
	
	def infoPrint(self):
		if self.keySelected:
			print(BColors.ORANGE+"\nSelected Key: "+BColors.CLEAR+BColors.OKGREEN+BColors.UNDERLINE+f"{self.pathKey}\n" +BColors.CLEAR)
		if self.pathSelected:
			print(BColors.ORANGE+"\nSelected Passfile: "+BColors.CLEAR+BColors.OKGREEN+BColors.UNDERLINE+f"{self.pathFile}\n"+BColors.CLEAR)
	
	def resetSelection(self):
		self.keySelected = False
		self.pathKey = None
		self.pathSelected = False
		self.pathFile = None
	
	def initPassmanager(self, fileDir, keyDir):
		print('>>> P455 W1ZZ4RD started.\n>>> System: initialize relevant data ...')
		sleep(1.5)
		if not os.path.exists('data'):
			print(BColors.VIOLETT+'>>> System: No Savedirectorys found! Create dat directory...'+BColors.CLEAR)
			os.mkdir('data/')
		if not os.path.exists('data/'+fileDir):
			print(BColors.VIOLETT+'>>> System: No '+fileDir+' dir. Create one...'+BColors.CLEAR)
			os.mkdir('data/'+fileDir)
		if not os.path.exists('data/'+keyDir):
			print(BColors.VIOLETT+'>>> System: No '+keyDir+' dir. Create one...'+BColors.CLEAR)
			os.mkdir('data/'+keyDir)
		print('>>> System: Data directory:'+BColors.OKGREEN+' okay!'+BColors.CLEAR)
		print('>>> System: '+keyDir+' directory:'+BColors.OKGREEN+' okay!'+BColors.CLEAR)
		print('>>> System: '+fileDir+' directory:'+BColors.OKGREEN+' okay!'+BColors.CLEAR)
		print(BColors.OKGREEN+'>>> Systen: all checks okay, start software...'+BColors.CLEAR)
		sleep(3)
	def banner(self):
		return print(BColors.BOLD+BColors.OKCYAN+(r"""
 ______    __     _______  _______    _  _  _   __  _______  _______  __     ______   _____   
(_____ \  / /    (_______)(_______)  | || || | /  |(_______)(_______)/ /    (_____ \ (____ \  
 _____) )/ /____  ______   ______    | || || |/_/ |   __       __   / /____  _____) ) _   \ \ 
|  ____/|___   _)(_____ \ (_____ \   | ||_|| |  | |  / /      / /  |___   _)(_____ ( | |   | |
| |         | |   _____) ) _____) )  | |___| |  | | / /____  / /____   | |        | || |__/ / 
|_|         |_|  (______/ (______/    \______|  |_|(_______)(_______)  |_|        |_||_____/  
			
   			-Version 0.2.1 | Copyright © 2022 S3R43o3-
""")+BColors.CLEAR)
	
	def menu(self):
		return print(BColors.ORANGE+BColors.BOLD+(f"""\n
{BColors.OKCYAN+BColors.BOLD+"Welcome! What do you want to do?"+BColors.CLEAR+BColors.ORANGE+BColors.BOLD}
{BColors.OKCYAN+BColors.BOLD+"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"}
	{BColors.OKCYAN+"Selected Key: "+BColors.CLEAR+BColors.ORANGE+BColors.BOLD} {self.pathKey}
	{BColors.OKCYAN+"Selected Pass-File: "+BColors.CLEAR+BColors.ORANGE+BColors.BOLD} {self.pathFile}
 
		(1) Create a new password key
		(2) Load an existing password key

		(3) Create new password file
		(4) Load existing password file

		(5) Add a new password
		(6) Get a password
		
		(r) Reset selection
		

		(q) Quit              
	"""+BColors.CLEAR))
	 

	
def main():
	password = {
		"PLACEHOLDER-PASS-1": "743z4782",
	}
	
	pm = PasswordManager()
	clearConsole()
# 	print(BColors.BOLD+BColors.OKCYAN+(r"""
#  ______    __     _______  _______    _  _  _   __  _______  _______  __     ______   _____   
# (_____ \  / /    (_______)(_______)  | || || | /  |(_______)(_______)/ /    (_____ \ (____ \  
#  _____) )/ /____  ______   ______    | || || |/_/ |   __       __   / /____  _____) ) _   \ \ 
# |  ____/|___   _)(_____ \ (_____ \   | ||_|| |  | |  / /      / /  |___   _)(_____ ( | |   | |
# | |         | |   _____) ) _____) )  | |___| |  | | / /____  / /____   | |        | || |__/ / 
# |_|         |_|  (______/ (______/    \______|  |_|(_______)(_______)  |_|        |_||_____/  
			
#    			-Version 0.2.1 | Copyright © 2022 S3R43o3-
# """)+BColors.CLEAR)
# 	menu = print(BColors.ORANGE+BColors.BOLD+(f"""\n
# {BColors.OKCYAN+BColors.BOLD+"Welcome! What do you want to do?"+BColors.CLEAR+BColors.ORANGE+BColors.BOLD}
# {BColors.OKCYAN+BColors.BOLD+"‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"}
# 	{BColors.OKCYAN+"Selected Key: "+BColors.CLEAR+BColors.ORANGE+BColors.BOLD} {pm.pathKey}
# 	{BColors.OKCYAN+"Selected Pass-File: "+BColors.CLEAR+BColors.ORANGE+BColors.BOLD} {pm.pathFile}
 
# 		(1) Create a new password key
# 		(2) Load an existing password key

# 		(3) Create new password file
# 		(4) Load existing password file

# 		(5) Add a new password
# 		(6) Get a password
		
# 		(r) Reset selection
		

# 		(q) Quit              
# 	"""+BColors.CLEAR))
	if(pm.fistRun):
		pm.banner()
	pm.initPassmanager('file','keys')
	pm.menu()
	done = False
	while not done:
		try:
			#pm.infoPrint()
			choice = input(BColors.BOLD+BColors.OKBLUE+"Enter a Option: "+BColors.CLEAR)
			if choice == "1":
				#pm.infoPrint()
				path = input(BColors.BOLD+BColors.OKBLUE+"Enter keyname: "+BColors.CLEAR)
				if path.lower() == 'q':
					return main()
				pm.createKey(path)
			elif choice == "2":            
				#pm.infoPrint()
				savedKeys = os.listdir('data/keys')
				if savedKeys == "":
					print(BColors.BOLD+BColors.RED+"\nNo key exist! Please create a key first!\n"+BColors.CLEAR)
					sleep(2)
					return main()
				print(BColors.BOLD+BColors.ORANGE+'\nYour saved keys: \n'+BColors.CLEAR)
				count= 0
				for key in savedKeys:
					size = len(key)
					key = key[:size -4]
					count +=1
					print(BColors.BOLD+BColors.OKGREEN+f"	{str(count)}) "+key+BColors.CLEAR)
				path = input(BColors.BOLD+BColors.OKBLUE+"\nEnter keyname to load: "+BColors.CLEAR)					
				if path.lower() == 'q':
					return main()
				pm.loadKey(path)
				pm.menu()
			elif choice == "3":
				if not pm.keySelected:
					print(BColors.BOLD+BColors.RED+'\n>>>>>>>>>> You need to select a passwordkey first! <<<<<<<<<<\n'+BColors.CLEAR)
					sleep(2.0)
					return main()
				#pm.infoPrint()		
				path = input(BColors.BOLD+BColors.OKBLUE+"Enter a name for new passwordfile: "+BColors.CLEAR)
				if path.lower() == 'q':
					return main()
				pm.createPassFile(path, password)
				pm.menu()
			elif choice == "4":
				if not pm.keySelected:
					print(BColors.BOLD+BColors.RED+'\n>>>>>>>>>> You need to select a passwordkey first! <<<<<<<<<<\n'+BColors.CLEAR)
					sleep(2.0)
					return main()
				#pm.infoPrint()
				savedFiles = os.listdir('data/files')
				count = 0
				print(BColors.BOLD+BColors.ORANGE+'\nYour saved passfiles: \n'+BColors.CLEAR)
				for file in savedFiles:
						size = len(file)
						file = file[:size-5]
						count += 1	
						print(BColors.BOLD+BColors.OKGREEN+f"	{str(count)}) "+file+BColors.CLEAR)
				path = input(BColors.BOLD+BColors.OKBLUE+"\nEnter the name of passwordfile to load: "+BColors.CLEAR)
				if path.lower() == 'q':
					return main()
				pm.loadPassFile(path)
				pm.menu()
			elif choice == "5":
				if not pm.keySelected:
					print(BColors.BOLD+BColors.RED+'\n>>>>>>>>>> You need to select a passwordkey first! <<<<<<<<<<\n'+BColors.CLEAR)
					sleep(2.0)
					return main()
				#pm.infoPrint()
				site = input(BColors.BOLD+BColors.OKBLUE+"Enter site: "+BColors.CLEAR)
				password = input(BColors.BOLD+BColors.OKBLUE+"Enter password: "+BColors.CLEAR)
				if password.lower() == 'q' | site.lower() == 'q':
					print('\nBack to mainmenu')
					sleep(1.5)
					return main()
				pm.addPassword(site,password)
				pm.menu()
			elif choice == "6":
				if not pm.keySelected:
					print(BColors.BOLD+BColors.RED+'\n>>>>>>>>>> You need to select a passwordkey first! <<<<<<<<<<\n'+BColors.CLEAR)
					sleep(2.0)
					return main()
				site = input(BColors.BOLD+BColors.OKBLUE+"What site password you want?: "+BColors.CLEAR)
				if site.lower() == 'q':
					return main()
				pm.menu()
				print(BColors.ORANGE+BColors.BOLD+f"Password for {BColors.OKGREEN+site+BColors.CLEAR+BColors.ORANGE+BColors.BOLD} is {BColors.OKGREEN+pm.getPassword(site)+BColors.CLEAR}")
			elif choice.lower() == "q":
				done = True
				print(BColors.RED+BColors.BOLD+"\n <<<<< Bye! >>>>>\n\n"+BColors.CLEAR)            
			elif choice.lower() == 'r':
				pm.resetSelection()
				print(BColors.ORANGE+BColors.BOLD+"\nYou can now choose a other key and file!\n")
			else:
				pm.errMsg()
				sleep(2.0)
				return main()
		except KeyboardInterrupt:
			print('\n exiting ...')
			quit(0)

if __name__=='__main__':
	clearConsole()
	
	main()        







