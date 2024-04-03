import os
import sys
import gg8lib
import colorama as c
import data as d
from time import sleep as wait

homePath = None

errc = {
    "-1": "Reset",
    "0": "Success",
    "1": "Fatal Failure"
}

if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", d.env, "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus", d.env, "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        print(homePath)
        raise OSError("TerminalPlus HOME is not valid")
else:
    raise OSError("TerminalPlus HOME is missing")

os.chdir(homePath)

ret = -1

while ret == -1:
    if len(sys.argv) > 1:
        ret = os.system(f"python {os.path.join(homePath, "code", "main.py")} {" ".join(sys.argv[1:])}")
    else:
        ret = os.system(f"python {os.path.join(homePath, "code", "main.py")}")
    
    if ret == -1:
        temp = 3
        print(f"{c.Fore.YELLOW}Exited program with code -1{c.Style.RESET_ALL} (Reset in {str(temp)})")
        wait(1)
        
        gg8lib._upAndClear()
        temp = 2
        print(f"{c.Fore.YELLOW}Exited program with code -1{c.Style.RESET_ALL} (Reset in {str(temp)})")
        wait(1)
        
        gg8lib._upAndClear()
        temp = 1
        print(f"{c.Fore.YELLOW}Exited program with code -1{c.Style.RESET_ALL} (Reset in {str(temp)})")
        wait(1)

if ret == 0:
    print(f"{c.Fore.GREEN}Exited program with code 0{c.Style.RESET_ALL} (Success)")
else:
    if errc.get(str(ret)):
        print(f"{c.Fore.RED}Exited program with code {str(ret)}{c.Style.RESET_ALL} ({errc[str(ret)]})")
    else:
        print(f"{c.Fore.RED}Exited program with code {str(ret)}{c.Style.RESET_ALL} (Unknown Failure)")