import os
import colorama as c

def upAndClear():
    print(LINE_UP, end=LINE_CLEAR)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

clone = input("[directory] Environment Directory: ")

while not os.path.isdir(clone):
    print(c.Fore.RED + "Not a valid directory.\n" + c.Style.RESET_ALL)
    clone = input("[directory] Environment Directory: ")

if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus", "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        raise OSError("TerminalPlus HOME is not valid")
else:
    raise OSError("TerminalPlus HOME is missing")

print()

os.system("clone \"" + homePath + "\" \"" + clone + "\"")