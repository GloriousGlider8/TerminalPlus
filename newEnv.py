import os
import colorama as c

clone = input("[directory] Environment Directory: ")
name = input("[string] (DIR Name) Environment Name: ")

while not os.path.isdir(clone):
    print(c.Fore.RED + "Not a valid directory.\n" + c.Style.RESET_ALL)
    clone = input("[directory] Environment Directory: ")

print()

os.mkdir(clone + "\\data")
os.mkdir(clone + "\\addons")
temp = open(clone + "\\data\\addonsdef.json", "x")
temp.write("[\"addon-test\"]")
temp.close()
temp = open(clone + "\\addons\\addon-test.py", "x")
temp.write("""import json
import colorama as c
argsTxt = open("args.json", "r")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None

temp = \"\"\"argsTxt = open(\"data\\\\args.json\", \"r\")
args = json.load(argsTxt)
argsTxt.close()
argsTxt = None\"\"\"

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
