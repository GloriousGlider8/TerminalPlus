######################################################################
#                      Terminal + CLI Forwarder                      #
#                      NT_10+11_**_py3.12.1_any                      #
######################################################################

import sys
import os

homePath = ""
def cmdExists(cmd):
    return os.system("cmd /c \"(help {0} > nul || exit 0) && where {0} > nul 2> nul\"".format(cmd)) == 0

def setHomePath(env: str):
    global homePath
    
    if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", env, "PATH")):
        homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus", env, "PATH"))
        homePath = homePathTxt.read()
        homePathTxt.close()
        homePathTxt = None
        if not os.path.exists(homePath):
            print(f"{homePath} is not valid.")
            print("Exited with code 1")
            exit(1)
    else:
        print(f"HOME or environment: {env} not found")
        print("Exited with code 1")
        exit(1)

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        if sys.argv[1] == "-I" or sys.argv[1] == "/i":
            setHomePath(sys.argv[2])
        else:
            setHomePath("MAIN")
        
        if not cmdExists("python"):
            print("Python executable not found in PATH")
            print("Exited with code 1")
            exit(1)

        if homePath == "MAIN":
            os.system(f"python \"{homePath}\\code\" {" ".join(sys.argv[1:])}")
        else:
            os.system(f"python \"{homePath}\\code\" {" ".join(sys.argv[3:])}")
    
else:
    setHomePath("MAIN")
    
    os.system(f"python \"{homePath}\\code\"")

exit(0)
