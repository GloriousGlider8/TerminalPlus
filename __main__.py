import data as d
import os
import runpy
import json
import datetime
import socket
import time
import requests
import keyboard as k
import colorama as c
import sys

ENVI = d.env
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

ip = socket.gethostbyname(socket.gethostname())
found = None
homePath = None
noExec = False
toExec = ""

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

if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", ENVI, "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus", ENVI, "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        raise OSError("TerminalPlus HOME is not valid")
else:
    raise OSError("TerminalPlus HOME is missing")

with open(homePath + "\\data\\li", "r") as file:
    lip = str(file.read())

    file.close()

    if lip != str(ip):
        os.remove(homePath + "\\data\\li")
        
        print("\nIP changed from " + lip + " to " + ip + "\n")

        with open(homePath + "\\data\\li", "w") as file1:
            file1.write(str(ip))

        time.sleep(1.5)

os.system("@echo off")
os.system("cls")

def cmdExists(cmd):
    return os.system("cmd /c \"(help {0} > nul || exit 0) && where {0} > nul 2> nul\"".format(cmd)) == 0

if not cmdExists("python"):
    if selPrompt(["Yes", "No"], [">", ">"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
        os.system("python")

def log(content, typ):
    logs = open(homePath + "\\data\\termP.log", "a")

    logs.write("\n{0} [{1}] [{2}] [{3}] {4}".format(os.getenv("COMPUTERNAME") + "\\" + os.getenv("USERDOMAIN") + "\\" + os.getenv("USERNAME"), str(ip), typ, str(datetime.datetime.now()).split(" ")[1].split(".")[0], content))

    logs.close()

def clearLog():
    os.remove(homePath + "\\data\\termP.log")

    logs = open(homePath + "\\data\\termP.log", "x")

    logs.write("{0} [{1}] [{2}] [{3}] {4}".format(os.getenv("COMPUTERNAME") + "\\" + os.getenv("USERDOMAIN") + "\\" + os.getenv("USERNAME"), str(ip), "INFO", str(datetime.datetime.now()).split(" ")[1].split(".")[0], "Logs Cleared"))

    logs.close()

def ftlKBI():
    logs = open(homePath + "\\data\\termP.log", "a")

    logs.write("\n{0} [{1}] [{2}] [{3}] {4}".format(os.getenv("COMPUTERNAME") + "\\" + os.getenv("USERDOMAIN") + "\\" + os.getenv("USERNAME"), str(ip), "FATAL", str(datetime.datetime.now()).split(" ")[1].split(".")[0], "Keyboard Crash (CTRL+C)"))

    logs.close()

os.system("cls")

log("User loaded program", "STARTUP")

temp = c.Fore.YELLOW

temp1 = [3, 10, 11]

temp2 = sys.version.split(" ")[0].split(".")

temp3 = True

for i in range(len(temp2)):
    temp2[i] = int(temp2[i])

if temp2[0] != temp1[0]:
    temp = c.Fore.RED

    temp3 = False

if temp3 and temp2[1] == temp1[1]:
    temp = c.Fore.GREEN

for i in range(len(temp2)):
    temp2[i] = str(temp2[i])

about = """
**************************************************

--- About Terminal + ---

    Version: NT_10+11_1.0.6_py3.10.11_usr
    System: NT
    System Version: Windows 10 / 11
    Terminal + Software Version: 1.0.6
    Intended Python Interpreter Version: {13}3.10.11{15}
    Current Python Interpreter Version: {13}{14}{15}
    Terminal + Installation Type: User Account
    Terminal + HOME: {16}
    Environment: {17}

--- About Your Profile ---

User: {0}
User Profile: {1}
AppData: {2}
Domain: {3}

--- About This System ---

PC Name: {4}
System Drive: {5}
Processor Count: {6}
Processor Architecture: {7}
Processor Identifier: {8}
Processor Level: {9}
CPU Count: {10}

--- Private Info ---

NOTE: None of this is ever sent without your consent!

(Stored in data\\termP.log) IP: {11}
(Stored in data\\li) Last IP: {12}

**************************************************

--- Terminal + ---
""".format(os.getenv("USERNAME"), os.getenv("USERPROFILE"), os.getenv("APPDATA"), os.getenv("USERDOMAIN"), os.getenv("COMPUTERNAME"), os.getenv("SYSTEMDRIVE"), os.getenv("NUMBER_OF_PROCESSORS"), os.getenv("PROCESSOR_ARCHITECTURE"), os.getenv("PROCESSOR_IDENTIFIER"), os.getenv("PROCESSOR_LEVEL"), str(os.cpu_count()), ip, lip, temp, ".".join(temp2), c.Style.RESET_ALL, homePath, ENVI)

print("--- Terminal + ---")

k.add_hotkey("ctrl+c", ftlKBI)

while True:
    try:
        if noExec:
            cmd = toExec
            noExec = False

            log(cmd, "AUTO_EXEC")
        else:
            cmd = input("\n" + os.getenv("COMPUTERNAME") + "\\" + os.getenv("USERDOMAIN") + "\\" + os.getenv("USERNAME") + " >> ")

            log(cmd, "MANUAL_EXEC")

            print("")
        
        if cmd.find(" && ") != -1:
            temp = cmd.split(" && ")

            cmd = temp[0]

            noExec = True
            toExec = " && ".join(temp[1:len(temp)])
        
        if cmd.find("&amp;") != -1:
            cmd = "&".join(cmd.split("&amp;"))
        if cmd.find("&nln;") != -1:
            cmd = "\n".join(cmd.split("&nln;"))
        if cmd.find("?ip;") != -1:
            if selPrompt(["No", c.Fore.YELLOW + "Yes" + c.Style.RESET_ALL], [">", "!"], "A source wants access to this device's IP address.\nAllow Access?\nWith an IP, a wifi network can easily be tracked!") == 0:
                cmd = "0".join(cmd.split("?ip;"))
            else:
                cmd = str(ip).join(cmd.split("?ip;"))
        if cmd.find("?pmt;") != -1:
            cmd = str(prompt).join(cmd.split("?pmt;"))

        args = cmd.split(" ")

        if args[0] == "exit":
            break
        elif args[0] == "pytest":
            if selPrompt(["Yes", "No"], [">", ">"], "You may not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
                if not cmdExists("pip"):
                    os.system("python")
                else:
                    print("Python is already installed")
        elif args[0] == "cmd":
            print("--- Windows NT Command Prompt ---\n")

            os.system("cmd")

            print("\n--- Terminal + ---\n")
        elif args[0] == "powershell" or args[0] == "ps":
            print("--- Windows NT PowerShell ---\n")

            os.system("powershell")

            print("\n--- Terminal + ---\n")
        elif args[0] == "bash":
            print("--- Bash ---\n")

            if cmdExists("bash"):
                os.system("bash")
            else:
                print("WSL is not enabled on your PC")

            print("\n--- Terminal + ---\n")
        elif args[0] == "env":
            if len(args) >= 4:
                if args[1] == "set":
                    os.system("set " + args[2] + "=" + args[3])
                    if os.getenv(args[2]) == args[3]:
                        print("Set Environment Variable: " + args[2] + " to: " + args[3])
                    else:
                        print("Failed to set environment variable")
            if len(args) >= 3:
                if args[1] == "get":
                    print(args[2] + " = " + os.getenv(args[2]))
        elif args[0] == "pyc" or args[0] == "pythonconsole" or args[0] == "python":
            print("--- Python Console ---\n")

            if cmdExists("pip"):
                os.system("python")
            else:
                if selPrompt(["Yes", "No"], [">", ">"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
                    os.system("python")

            print("\n--- Terminal + ---\n")
        elif args[0] == "pip":
            print("--- Preferred Installer Program (Python) ---\nInstall or uninstall packages from PyPi\n")
            if cmdExists("pip"):
                while True:
                    cmd = input("PIP >>> ")

                    if cmd != "exit":
                        os.system("pip " + cmd)
                    else:
                        break
            else:
                if selPrompt(["Yes", "No"], [">", ">"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
                    os.system("python")
            
            print("--- Terminal + ---\n")
        elif args[0] == "reg":
            print("--- Program Registration ---\n")
            silent = False
            if len(args) > 1:
                print("[filepath] File: " + args[1])
                reg = args[1]
                if len(args) > 2 and args[2] == "/s":
                    print("[true / false] Silent: true")
                    silent = True
                else:
                    if input("[true / false] Silent: ") == "true":
                        silent = True
            else:
                reg = input("[filepath] File: ")
                if input("[true / false] Silent: ") == "true":
                    silent = True
                
            if os.path.exists(reg):
                if not silent:
                    print("\nStarting Installation\n" + c.Fore.RED + "---------------------" + c.Style.RESET_ALL)

                    time.sleep(0.5)

                    upAndClear()
                    upAndClear()

                    print("Writing Configuration\n-------" + c.Fore.RED + "--------------" + c.Style.RESET_ALL)

                    time.sleep(1.5)

                    with open(homePath + "\\data\\addonsdef.json", "r") as temp1:
                        temp = json.load(temp1)

                    os.remove(homePath + "\\data\\addonsdef.json")

                    temp2 = input("[string] Command Name: ")
                    upAndClear()

                    with open(homePath + "\\data\\addonsdef.json", "w") as temp1:
                        temp.append(temp2)
                        temp1.write(json.dumps(temp))

                    upAndClear()
                    upAndClear()

                    print("Moving Source\n--------------" + c.Fore.RED + "-------" + c.Style.RESET_ALL)

                    time.sleep(2.5)

                    os.rename(reg, homePath + "\\data\\" + temp2 + ".py")

                    upAndClear()
                    upAndClear()

                    print("Registration Complete\n---------------------\n\nNew: " + temp2)

                    time.sleep(3)
                else:
                    time.sleep(1.5)

                    with open(homePath + "\\data\\addonsdef.json", "r") as temp1:
                        temp = json.load(temp1)

                    os.remove(homePath + "\\data\\addonsdef.json")

                    temp2 = input("[string] Command Name: ")
                    upAndClear()

                    with open(homePath + "\\data\\addonsdef.json", "w") as temp1:
                        temp.append(temp2)
                        temp1.write(json.dumps(temp))

                    time.sleep(2.5)

                    os.rename(reg, homePath + "\\data\\" + temp2 + ".py")

                    time.sleep(3)
            else:
                print("File: " + reg + " does not exist")
        elif args[0] == "version" or args[0] == "about":
            print(about)
        elif args[0] == "pausek":
            print("Execution is paused.\nTo resume, press [" + args[1].upper() + "] or [CTRL] & [C] to quit.")
            k.wait(args[1].lower())
        elif args[0] == "pause":
            print("Execution is paused.\nTo resume, press [SPACE] or [CTRL] & [C] to quit.")
            k.wait("space")
        elif args[0] == "restart" or args[0] == "reset":
            os.system("\"" + os.path.join(homePath, "code", "__main__.py") + "\"")
            time.sleep(10)
            break
        elif args[0] == "write":
            print(" ".join(args[1:len(args)]), end="")
        elif args[0] == "writeln":
            print(" ".join(args[1:len(args)]))
        elif args[0] == "error":
            print("ERR\nTYP: {0}\nARG: {1}".format(args[1], args[2,100]))
        elif args[0] == "crash":
            log("User Requested Crash", "FATAL")
            raise KeyboardInterrupt()
        elif args[0] == "prompt":
            prompt = input(">> ")
            log(prompt, "PROMPT")
        elif args[0] == "wait":
            time.sleep(float(args[1]))
        elif args[0] == "clearln":
            upAndClear()
        elif args[0] == "http":
            if args[1] == "get":
                print(str(requests.get(args[2], json.loads(" ".join(args[3:len(args)]))).content))
            elif args[1] == "post":
                print(str(requests.post(args[2], json.loads(" ".join(args[3:len(args)]))).content))
        elif args[0] == "ctest":
            get = "http://httpbin.org/get"
            post = "http://httpbin.org/post"

            if len(args) > 1:
                if len(args) == 2:
                    get = args[1]
                else:
                    get = args[1]
                    post = args[2]

            os.system("cls")

            print("Testing Connection\n-" + c.Fore.RED + "--------------------" + c.Style.RESET_ALL)
            
            bt = str(datetime.datetime.now()).split(" ")[1]

            print("Download\n" + get + "\n#:##:##\n" + c.Fore.YELLOW + "In Progress" + c.Style.RESET_ALL)
            
            temp1 = True

            try:
                response = requests.get(get)
                response.raise_for_status()
            except requests.exceptions.ConnectionError:
                getres = "CNC"
                temp1 = False
            except requests.exceptions.Timeout:
                getres = "TIM"
                temp1 = False
            except requests.exceptions.HTTPError as e:
                getres = str(e).split(" ")[0]
                temp1 = False
            except requests.exceptions.RequestException as e:
                getres = str(e).split(" ")[0]
                temp1 = False
            
            at = str(datetime.datetime.now()).split(" ")[1]

            t1 = datetime.datetime.strptime(bt, "%H:%M:%S.%f")

            t2 = datetime.datetime.strptime(at, "%H:%M:%S.%f")

            delta = t2 - t1

            dwn = delta
            
            if temp1:

                os.system("cls")

                print("Testing Connection\n-----------" + c.Fore.RED + "----------" + c.Style.RESET_ALL)
                print("Download\n" + get + "\n" + str(delta) + "\n" + c.Fore.GREEN + "Completed" + c.Style.RESET_ALL)

                temp3 = False
            else:

                os.system("cls")

                print("Testing Connection\n-" + c.Fore.RED + "!!!!" + getres + "!!!----------" + c.Style.RESET_ALL)
                print("Download\n" + get + "\n#:##:##\n" + c.Fore.RED + "Failed" + c.Style.RESET_ALL)

                temp3 = True
            bt = str(datetime.datetime.now()).split(" ")[1]

            upAndClear()
            upAndClear()
            upAndClear()
            upAndClear()

            print("Upload\n" + post + "\n#:##:##\n" + c.Fore.YELLOW + "In Progress" + c.Style.RESET_ALL)
            
            temp1 = True

            try:
                response = requests.post(post)
                response.raise_for_status()
            except requests.exceptions.ConnectionError:
                postres = "CNC"
                temp1 = False
            except requests.exceptions.Timeout:
                postres = "TIM"
                temp1 = False
            except requests.exceptions.HTTPError as e:
                postres = str(e).split(" ")[0]
                temp1 = False
            except requests.exceptions.RequestException as e:
                postres = str(e).split(" ")[0]
                temp1 = False
            
            at = str(datetime.datetime.now()).split(" ")[1]

            t1 = datetime.datetime.strptime(bt, "%H:%M:%S.%f")

            t2 = datetime.datetime.strptime(at, "%H:%M:%S.%f")

            delta = t2 - t1

            upl = delta

            if temp1:
                os.system("cls")

                if temp3:
                    print("Testing Connection\n-" + c.Fore.RED + "!!!!" + getres + "!!!" + c.Style.RESET_ALL + "----------")
                else:
                    print("Testing Connection\n---------------------")
                print("Upload\n" + post + "\n" + str(delta) + "\n" + c.Fore.GREEN + "Completed" + c.Style.RESET_ALL)
            else:
                os.system("cls")

                if temp3:
                    print("Testing Connection\n-" + c.Fore.RED + "!!!!" + getres + "!!!!!!!" + postres + "!!!" + c.Style.RESET_ALL)
                else:
                    print("Testing Connection\n-----------" + c.Fore.RED + "!!!!" + postres + "!!!" + c.Style.RESET_ALL)
                print("Upload\n" + post + "\n#:##:##\n" + c.Fore.RED + "Failed" + c.Style.RESET_ALL)

            os.system("cls")

            if temp3:
                print("GET: " + c.Fore.RED + "Failed" + c.Style.RESET_ALL + " in: " + str(dwn) + c.Fore.RED + " ERR" + c.Style.RESET_ALL)

                if getres == "CNC":
                    print(c.Fore.YELLOW + "GET Error: " + c.Fore.RED + "Connection Error" + c.Style.RESET_ALL)
                    log("Failed to GET " + get + " due to Connection Error", "ERROR")
                elif getres == "TIM":
                    print(c.Fore.YELLOW + "GET Error: " + c.Fore.RED + "Timeout" + c.Style.RESET_ALL)
                    log("Failed to GET " + get + " due to Timeout", "ERROR")
                else:
                    print(c.Fore.YELLOW + "GET Error: " + c.Fore.RED + "HTTP-" + getres + c.Style.RESET_ALL)
                    log("Failed to GET " + get + " due to HTTP-" + getres, "ERROR")
            else:
                if dwn < upl:
                    print("GET: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(dwn) + c.Fore.GREEN + " Λ" + c.Style.RESET_ALL)
                elif dwn == upl:
                    print("GET: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(dwn) + c.Fore.YELLOW + " =" + c.Style.RESET_ALL)
                else:
                    print("GET: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(dwn) + c.Fore.RED + " V" + c.Style.RESET_ALL)
            if temp1:
                if dwn > upl:
                    print("POST: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(upl) + c.Fore.GREEN + " Λ" + c.Style.RESET_ALL)
                elif dwn == upl:
                    print("POST: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(upl) + c.Fore.YELLOW + " =" + c.Style.RESET_ALL)
                else:
                    print("POST: " + c.Fore.GREEN + "Passed" + c.Style.RESET_ALL + " in: " + str(upl) + c.Fore.RED + " V" + c.Style.RESET_ALL)
            else:
                print("POST: " + c.Fore.RED + "Failed" + c.Style.RESET_ALL + " in: " + str(upl) + c.Fore.RED + " ERR" + c.Style.RESET_ALL)
                
                if postres == "CNC":
                    print(c.Fore.YELLOW + "POST Error: " + c.Fore.RED + "Connection Error" + c.Style.RESET_ALL)
                    log("Failed to POST to " + post + " due to Connection Error", "ERROR")
                elif postres == "TIM":
                    print(c.Fore.YELLOW + "POST Error: " + c.Fore.RED + "Timeout" + c.Style.RESET_ALL)
                    log("Failed to POST to " + post + " due to Timeout", "ERROR")
                else:
                    print(c.Fore.YELLOW + "POST Error: " + c.Fore.RED + "HTTP-" + postres + c.Style.RESET_ALL)
                    log("Failed to POST to " + post + " due to HTTP-" + postres, "ERROR")

            if get != "http://httpbin.org/get":
                print("Custom GET URL: " + get)
            if post != "http://httpbin.org/post":
                print("Custom POST URL: " + post)
            print("TOTAL: " + str(dwn + upl))
        elif args[0] == "rmv":
            if args[1] == "reg":
                print("\n--- Registration Removal ---\n")
                print("Reading command data\n" + c.Fore.RED + "---------------------" + c.Style.RESET_ALL)
                rmv = input("[string] Command to remove: ")
                upAndClear()
                upAndClear()
                upAndClear()
                print("Reading addon dictionary\n-------" + c.Fore.RED + "--------------" + c.Style.RESET_ALL)
                temp = open(homePath + "\\data\\addonsdef.json")
                temp1 = json.load(temp)
                temp.close()
                upAndClear()
                upAndClear()
                print("Editing addon dictionary\n--------------" + c.Fore.RED + "-------" + c.Style.RESET_ALL)
                os.remove(homePath + "\\data\\addonsdef.json")
                temp = open(homePath + "\\data\\addonsdef.json", "x")
                temp2 = []
                for v in temp1:
                    if v != rmv:
                        temp2.append(v)
                temp.write(json.dumps(temp2))
                temp.close()
                upAndClear()
                upAndClear()
                print("Removing script file\n--------------------" + c.Fore.RED + "-" + c.Style.RESET_ALL)
                if os.path.exists(homePath + "\\data\\" + rmv + ".py"):
                    os.remove(homePath + "\\data\\" + rmv + ".py")
                else:
                    raise IOError("Failed to delete addon script")
                upAndClear()
                upAndClear()
                print("Removed registration for " + rmv + "\n---------------------")
                print("\n--- Terminal + ---\n")
        elif args[0] == "clear":
            os.system("cls")
        elif args[0] == "log":
            if args[1] == "read":
                temp = open(homePath + "\\data\\termP.log")
                temp1 = temp.read()
                temp.close()
                temp1 = str(c.Fore.RED + "FATAL" + c.Style.RESET_ALL).join(temp1.split("FATAL"))
                temp1 = str(c.Fore.YELLOW + "ERROR" + c.Style.RESET_ALL).join(temp1.split("ERROR"))
                temp1 = str(c.Fore.BLUE + "INFO" + c.Style.RESET_ALL).join(temp1.split("INFO"))
                temp1 = str(c.Fore.GREEN + "STARTUP" + c.Style.RESET_ALL).join(temp1.split("STARTUP"))
                print("\n--- Logs ---\n")
                print(temp1)
                print("\n--- Terminal + ---\n")
            elif args[1] == "write":
                log("[" + args[2] + "] " + str(" ").join(args[3:len(args) - 1]), args[len(args) - 1])
            elif args[1] == "clear":
                print("Cleared the logs")
                clearLog()
        elif args[0] == "dev":
            print("\n--- Development Environment Setup ---\n")
            if selPrompt(["Yes", "No"], [">", "<"], "Are you sure you would like to setup a new environment?") == 0:
                runpy.run_path(homePath + "\\code\\newEnv.py")
        else:
            found = False
            temp = open(homePath + "\\data\\addonsdef.json")

            temp1 = json.load(temp)

            for i in range(len(temp1)):
                if temp1[i] == args[0]:
                    found = True
                    temp.close()
                    temp = None
                    break
            
            if found:
                os.remove(homePath + "\\data\\args.json")
                
                temp = open(homePath + "\\data\\args.json", "w")
                temp.write(json.dumps(args))
                temp.close()

                runpy.run_path(homePath + "\\data\\" + args[0] + ".py")
            else:
                print("Unknown command: " + args[0] + "\nIf this is an addon command, you can install it with the command reg\nIf you have already installed it, use rmv reg " + args[0] + " and then reg again.")

    except Exception as ex:
        template = "ERR\nTYP: {0}\nARG: {1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

        log("Exception: " + type(ex).__name__ + " {0!r}".format(ex.args), "ERROR")
#    finally:
#        print("")

os.system("cls")