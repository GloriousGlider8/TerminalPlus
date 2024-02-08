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
temp = open(clone + "\\data\\args.json", "x")
temp.write("[]")
temp.close()
temp = open(clone + "\\data\\li", "x")
temp.close()
temp = open(clone + "\\data\\termP.log", "x")
temp.close()
os.system("git clone https://github.com/GloriousGlider8/TerminalPlus \"" + clone + "\\code\"")
os.rename(f"{clone}\\code\\addon-test.py", f"{clone}\\addons\\addon-test.py")
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
