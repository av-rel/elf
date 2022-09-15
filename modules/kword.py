#Modules of keywords of shell console

def kword(args):

	from modules import ls

	if args == "help":
		ls.list();
	elif args == "del" or "ls" or "make" or "self" or "hello":
		pass
	else:
		print('Invalid command | Input help for instructions\n')