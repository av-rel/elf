from sys import argv
from colorama import Fore, Back, Style, init
from os import getcwd, listdir, remove
from sys import exit, getsizeof
from modules import kword

def __console(*argv):

	init(autoreset=True);

	try:
		while True:
			print(f'{Fore.LIGHTGREEN_EX}{getcwd()} {Fore.LIGHTRED_EX}->', end=" ")
			cmd = list(input().strip().lower().split())
			kword.kword(cmd[0]);

			if len(cmd) == 2 and cmd[0] == 'del':
				try:
					remove(cmd[1]);
				except:
					print("File doesn't exist\n")
					__console(*argv);

			elif cmd[0] == 'ls':
					for i in listdir():
						print(i);
					print('\n');

			elif cmd[0] == 'make':
				try:
					with open(cmd[1], 'w') as f:
							f.write(cmd[2]);
							f.close();
				except:
					__console(*argv);

			elif cmd[0] == 'self':
				print(*argv);
				print('\n');

			elif cmd[0] == 'hello':
				print("Hello\n");

			else: 
				__console(*argv);
			
	except KeyboardInterrupt:
		__console(*argv);
	except IndexError:
		__console(*argv);
	except:
		exit();

__console(*argv);