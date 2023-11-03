import os
import data as d
import colorama as c
import keyboard as k

clone = input("[directory] Environment Directory: ")
name = input("[string] (DIR Name) Environment Name: ")

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
temp.write("[\"addon-test\"]")
temp.close()
temp = open(clone + "\\data\\addon-test.py", "x")
temp.write("""import json
import colorama as c
argsTxt = open("args.json", "r")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None

temp = \"\"\"
argsTxt = open(\"data\\args.json\", \"r\")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None
\"\"\"

print(c.Fore.GREEN + \"Terminal + addons are working.\" + c.Style.RESET_ALL + \"\nArgument Format:\")
for i in range(len(args)):
    print(\"[\" + str(i) + \"]: \" + args[i])
print(c.Fore.BLUE + \"\nGet argument list with:\n\" + c.Fore.LIGHTCYAN_EX + temp)
print(c.Fore.BLUE + \"in your addon script.\" + c.Style.RESET_ALL)
""")
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