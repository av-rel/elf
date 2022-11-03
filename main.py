from sys import argv
from colorama import Fore, Back, Style, init
from os import getcwd, listdir, remove
from sys import exit, getsizeof
from modules import kword


def __console(*argv):

    init(autoreset=True)

    try:
        while True:

            print(f'{Fore.LIGHTGREEN_EX}{getcwd()} {Fore.LIGHTRED_EX}->', end=" ")
            cmd = list(input().strip().lower().split())
            kword.kword(cmd[0])

            if cmd[0] == 'del':
                try:
                    remove(cmd[1])
                    print(f"File {cmd[1]} deleted")
                except IndexError:
                    print("No file metioned to delete")
                    __console(*argv)
                except:
                    print(f"File {cmd[1]} doesn't exist")
                    __console(*argv)

            elif cmd[0] == 'ls':
                for i in listdir():
                    print(i)

            elif cmd[0] == "exit":
                exit()

            elif cmd[0] == 'make':
                try:
                    with open(cmd[1], 'w') as f:
                        f.write(cmd[2])
                        f.close()
                    print(f"Written file {cmd[0]}")
                except IndexError:
                    print("No file mentioned to add")
                except:
                    __console(*argv)

            else:
                __console(*argv)

    except KeyboardInterrupt:
        __console(*argv)
    except IndexError:
        __console(*argv)
    except:
        exit()


__console(*argv)
