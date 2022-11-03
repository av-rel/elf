from modules import ls


def kword(args):

    if args == "--help":
        ls.list()
        return
    elif args == "-h":
        ls.list()
        return
    elif args == "del" or "ls" or "make" or "self" or "hello":
        return
    
    print("Invalid command")
