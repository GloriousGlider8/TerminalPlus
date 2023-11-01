import os
import data as d
import colorama as c
import keyboard as k
import time
import runpy

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

def upAndClear():
    print(LINE_UP, end=LINE_CLEAR)

def selPrompt(options, icons, intro):
    os.system("cls")
    print(intro)
    print("\nUse [UP] and [DOWN] to move cursor.\nUse [RIGHT] to select.\n")

    print("[" + icons[0] + "] " + options[0])

    for i in range(len(options) - 1):
        print("[ ] " + options[i + 1])

    temp = 0
    temp1 = 0

    while True:
        time.sleep(0.15)

        if temp1 != temp:
            for _ in range(len(options)):
                upAndClear()
            for i in range(len(options)):
                if temp == i:
                    print("[" + icons[i] + "] " + options[i])
                else:
                    print("[ ] " + options[i])
                
            temp1 = temp

        if k.is_pressed("up"):
            if temp > 0:
                temp = temp - 1
                                    
        elif k.is_pressed("down"):
            if temp < len(options) - 1:
                temp = temp + 1

        elif k.is_pressed("right"):
            os.system("cls")
            return temp

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

clone = input("[directory] Environment Directory: ")
name = input("[string] (W/OUT Spaces) (DIR Name) Environment Name: ")

while not os.path.isdir(clone):
    print(c.Fore.RED + "Not a valid directory.\n" + c.Style.RESET_ALL)
    clone = input("[directory] Environment Directory: ")

if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", d.env, "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus",d.env , "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        raise OSError("TerminalPlus HOME is not valid")
else:
    raise OSError("TerminalPlus HOME is missing")

print()

os.mkdir(clone + "\\data")
temp = open(clone + "\\data\\addonsdef.json", "x")
temp.write("[]")
temp.close()
temp = open(clone + "\\data\\args.json", "x")
temp.write("[]")
temp.close()
temp = open(clone + "\\data\\li", "x")
temp.close()
temp = open(clone + "\\data\\termP.log", "x")
temp.close()
os.system("git clone https://github.com/GloriousGlider8/TerminalPlus \"" + clone + "\\code\"")
os.system("rmdir \"" + clone + "\\code\\.git\" /S /Q")
os.remove(clone + "\\code\\.gitignore")
os.mkdir(os.getenv("AppData") + "\\TerminalPlus\\" + name)
temp = open(os.getenv("AppData") + "\\TerminalPlus\\" + name + "\\PATH", "x")
temp.write(clone)
temp.close()
temp = open(clone + "\\code\\data.py")
temp1 = temp.readlines()
temp.close()
temp1[0] = "env = \"" + name + "\""
os.remove(clone + "\\code\\data.py")
temp = open(clone + "\\code\\data.py", "x")
for v in temp1:
    temp.write(v + "\n")
temp.close()
if selPrompt(["Yes", "No"], [">", ">"], "Would you like to open the alternitive environment now?") == 0:
    runpy.run_path(clone + "\\code\\__main__.py")