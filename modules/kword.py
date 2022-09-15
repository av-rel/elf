#Modules of keywords of shell console

def __kword(args):

	from modules import ls

	match args:

		case "help":
			ls.__list();
		case "del":
			pass
		case "ls":
			pass
		case 'make':
			pass
		case 'self':
			pass
		case 'hello':
			pass
		case default:
			print('Invalid command | Input help for instructions\n')