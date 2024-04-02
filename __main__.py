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
import gg8lib as f
import glob as g
import sys

noExec = False
toExec = ""
cliExec = False

if os.name == "posix":
    clearCmd = "clear"
elif os.name == "nt":
    clearCmd = "cls"
else:
    raise OSError(f"{c.Fore.RED}Invalid OS!{c.Style.RESET_ALL}")

if len(sys.argv) > 1:
    if sys.argv[1] == "/c" or sys.argv[1] == "-C":
        toExec = " ".join(sys.argv[2:]) + " && exit"
        noExec = True
        cliExec = True
    elif sys.argv[1] == "/?" or sys.argv[1] == "--help":
        cliExec = True
        noExec = True
        toExec = "exit"

pcname = os.getenv("COMPUTERNAME")
domain = os.getenv("USERDOMAIN")
uname = os.getenv("USERNAME")

PREF_VER = d.py_ver
ENVI = d.env
VER = d.ver

ip = socket.gethostbyname(socket.gethostname())
found = None
homePath = None

if os.path.exists(os.path.join(os.getenv("APPDATA"), "TerminalPlus", ENVI, "PATH")):
    homePathTxt = open(os.path.join(os.getenv("APPDATA"), "TerminalPlus", ENVI, "PATH"))
    homePath = homePathTxt.read()
    homePathTxt.close()
    homePathTxt = None
    if not os.path.exists(homePath):
        print(homePath)
        raise OSError("TerminalPlus HOME is not valid")
else:
    raise OSError("TerminalPlus HOME is missing")

os.chdir(homePath)

with open(homePath + "/data/li", "r") as file:
    lip = str(file.read())

    file.close()

    if lip != str(ip):
        os.remove(homePath + "/data/li")
        
        print("\nPrivate IP changed from " + lip + " to " + ip + "\n")

        with open(homePath + "/data/li", "w") as file1:
            file1.write(str(ip))

        time.sleep(1.5)

os.system("@echo off")
if not cliExec:
    os.system(clearCmd)

def cmdExists(cmd):
    return os.system("cmd /c \"(help {0} > nul || exit 0) && where {0} > nul 2> nul\"".format(cmd)) == 0

if not cmdExists("python"):
    if f.selPrompt(["Yes", "No"], [">", ">"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
        os.system("python")

def log(content, typ):
    logs = open(homePath + "/data/termP.log", "a")

    logs.write("\n{0} [{1}] [{2}] [{3}] {4}".format(pcname + "/" + domain + "/" + uname, str(ip), typ, str(datetime.datetime.now()).split(" ")[1].split(".")[0], content))

    logs.close()

def clearLog():
    os.remove(homePath + "/data/termP.log")

    logs = open(homePath + "/data/termP.log", "x")

    logs.write("{0} [{1}] [{2}] [{3}] {4}".format(pcname + "/" + domain + "/" + uname, str(ip), "INFO", str(datetime.datetime.now()).split(" ")[1].split(".")[0], "Logs Cleared"))

    logs.close()

def ftlKBI():
    logs = open(homePath + "/data/termP.log", "a")

    logs.write("\n{0} [{1}] [{2}] [{3}] {4}".format(pcname + "/" + domain + "/" + uname, str(ip), "FATAL", str(datetime.datetime.now()).split(" ")[1].split(".")[0], "Keyboard Crash (CTRL+C)"))

    logs.close()

log("User loaded program", "STARTUP")

temp = c.Fore.YELLOW

temp1 = PREF_VER

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

if os.name == "nt":
    systemName = "Microsoft NT (e.g. Windows)"
else:
    systemName = "Unix-based (e.g. Linux, Mac)"

about = """
**************************************************

--- About Terminal + ---

Version: {19}_{18}_py{21}_usr
    System: {20}
    Terminal + Software Version: {18}
    Intended Python Interpreter Version: {13}{21}{15}
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

(Stored in data/termP.log) IP: {11}
(Stored in data/li) Last IP: {12}

**************************************************

--- Terminal + ---
""".format(os.getenv("USERNAME"), os.getenv("USERPROFILE"), os.getenv("APPDATA"), os.getenv("USERDOMAIN"), os.getenv("COMPUTERNAME"), os.getenv("SYSTEMDRIVE"), os.getenv("NUMBER_OF_PROCESSORS"), os.getenv("PROCESSOR_ARCHITECTURE"), os.getenv("PROCESSOR_IDENTIFIER"), os.getenv("PROCESSOR_LEVEL"), str(os.cpu_count()), ip, lip, temp, ".".join(temp2), c.Style.RESET_ALL, homePath, ENVI, VER, os.name.upper(), systemName, str(temp1[0]) + "." + str(temp1[1]) + "." + str(temp1[2]))

if not cliExec:
    print("--- Terminal + ---")

k.add_hotkey("ctrl+c", ftlKBI)

while True:
    try:
        if noExec:
            cmd = toExec
            noExec = False

            log(cmd, "AUTO_EXEC")
        else:
            cmd = input("\n" + pcname + "/" + domain + "/" + uname + " >> ")

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
            if f.selPrompt(["No", c.Fore.YELLOW + "Yes" + c.Style.RESET_ALL], [">", "!"], "A source wants access to this device's private IP address.\nAllow Access?\nThis is a private IP and NOT a public one!") == 0:
                cmd = "0".join(cmd.split("?ip;"))
            else:
                cmd = str(ip).join(cmd.split("?ip;"))
        if cmd.find("?pmt;") != -1:
            cmd = str(prompt).join(cmd.split("?pmt;"))

        args = cmd.split(" ")

        if args[0] == "exit":
            break
        elif args[0] == "pytest":
            if f.selPrompt(["Yes", "No"], [">", "<"], "You may not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
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
                    os.system("set " + args[2] + " = " + args[3])
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
                if f.selPrompt(["Yes", "No"], [">", "<"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
                    os.system("python")

            print("\n--- Terminal + ---\n")
        elif args[0] == "pip":
            print("--- Preferred Installer Program (Python) ---\n")
            if cmdExists("pip"):
                while True:
                    cmd = input("PIP >>> ")

                    if cmd != "exit":
                        os.system("pip " + cmd)
                    else:
                        break
            else:
                if f.selPrompt(["Yes", "No"], [">", "<"], "You do not have python installed correctly on your computer.\nUsing addons and other features requires python.\nWould you like to install it?") == 0:
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
                    
                    if silent:
                        f._upAndClear()
                        print(f"[true / false] Silent: {c.Fore.GREEN}true{c.Style.RESET_ALL}")
                    else:
                        f._upAndClear()
                        print(f"[true / false] Silent: {c.Fore.RED}false{c.Style.RESET_ALL}")
            else:
                reg = input("[filepath] File: ")
                if input("[true / false] Silent: ") == "true":
                    silent = True
                
            if os.path.exists(reg):
                if not silent:
                    print()

                    prg = f.progressBar("Starting Registration", 21, c.Fore.GREEN, c.Fore.LIGHTGREEN_EX, c.Fore.CYAN)
                    prg.render()

                    prg.increase(7)
                    prg.setTitle("Writing Configuration")

                    time.sleep(0.5)

                    f._upAndClear()
                    f._upAndClear()

                    prg.render()

                    prg.increase(7)
                    prg.setTitle("Moving Source")

                    time.sleep(1.5)

                    with open(homePath + "/data/addonsdef.json", "r") as temp1:
                        temp = json.load(temp1)

                    temp2 = input("[string] Command Name: ")
                    f._upAndClear()

                    with open(homePath + "/data/addonsdef.json", "w") as temp1:
                        temp.append(temp2)
                        temp1.write(json.dumps(temp))

                    f._upAndClear()
                    f._upAndClear()

                    prg.render()

                    prg.increase(7)
                    prg.setTitle("Registration Complete")

                    time.sleep(2.5)

                    if os.system("copy " + reg + " " + homePath + "/addons/" + temp2 + ".py") != 0:
                        raise Exception(f"{c.Fore.RED}Failed to install!{c.Style.RESET_ALL}")

                    prg.render()
                    prg.keyMode(False)
                    os.system(clearCmd)

                    print("New: " + temp2)

                    time.sleep(3)
                else:
                    time.sleep(1.5)

                    with open(homePath + "/data/addonsdef.json", "r") as temp1:
                        temp = json.load(temp1)

                    os.remove(homePath + "/data/addonsdef.json")

                    temp2 = input("[string] Command Name: ")
                    f._upAndClear()

                    with open(homePath + "/data/addonsdef.json", "w") as temp1:
                        temp.append(temp2)
                        temp1.write(json.dumps(temp))

                    time.sleep(2.5)

                    if os.system("copy " + reg + " " + homePath + "/addons/" + temp2 + ".py") != 0:
                        raise Exception(f"{c.Fore.RED}Failed to install!{c.Style.RESET_ALL}")

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
            print("ERR\nTYP: {0}\nARG: {1}".format(args[1], tuple(args[2:100])))
        elif args[0] == "crash":
            log("User Requested Crash", "FATAL")
            raise KeyboardInterrupt()
        elif args[0] == "prompt":
            prompt = input(">> ")
            log(prompt, "PROMPT")
        elif args[0] == "wait":
            time.sleep(float(args[1]))
        elif args[0] == "clearln":
            f._upAndClear()
        elif args[0] == "http":
            if args[1] == "get":
                print(str(requests.get(args[2], json.loads(" ".join(args[3:len(args)]))).content))
            elif args[1] == "post":
                print(str(requests.post(args[2], json.loads(" ".join(args[3:len(args)]))).content))
        elif args[0] == "pkg":
            if args[1] == "install":
                print(f"Using {c.Fore.BLUE}GitHub{c.Style.RESET_ALL} for package search...")
                split = input("[string] GitHub Repo (author/repo/branch): ").split("/")
                
                author = split[0]
                repo = split[1]
                
                if len(split) < 3:
                    branch = "main"
                else:
                    branch = split[2]
                    
                prg = f.progressBar(f"Installing package: {" ".join(split)}", 2, c.Fore.GREEN, c.Fore.LIGHTGREEN_EX, c.Fore.LIGHTBLUE_EX)
                
                try:
                    data = requests.get(f"https://raw.githubusercontent.com/{author}/{repo}/{branch}/data.jsonc").content
                    if not os.path.exists(f"{homePath}/pkg"):
                        os.mkdir(f"{homePath}/pkg")
                    with open(f"{homePath}/pkg/data.json", "w") as dataf:
                        for v in data.decode("utf-8").split("\n"):
                            if v != "" and not v.startswith("//"):
                                dataf.write(f"{v.split("//")[0]}\n")
                    with open(f"{homePath}/pkg/data.json", "r") as dataf:
                        data = json.load(dataf)
                    prg.log("--- Package Data ---")
                    prg.log(f"{c.Fore.BLUE}Name {c.Style.RESET_ALL}{data["name"]}")
                    prg.log(f"{c.Fore.BLUE}Version {c.Style.RESET_ALL}{data["ver"]}")
                    prg.log(f"{c.Fore.BLUE}Command Name {c.Style.RESET_ALL}{data["cmd"]}")
                    if data["readme"]:
                        temp = f"{c.Fore.GREEN}Yes{c.Style.RESET_ALL}"
                    else:
                        temp = f"{c.Fore.RED}No{c.Style.RESET_ALL}"
                    prg.log(f"{c.Fore.BLUE}README installed {c.Style.RESET_ALL}{temp}")
                    prg.log(f"{c.Fore.BLUE}Dependencies:{c.Style.RESET_ALL}")
                    for v in data["pkg"]:
                        prg.log(f"• {v}")
                    if len(data["pkg"]) < 1:
                        prg.log(f"• None")
                    time.sleep(1)
                    
                    prg.increase(1)
                    prg.log("Gathering Scripts")
                    
                    time.sleep(1.5)
                    
                    init = requests.get(f"https://raw.githubusercontent.com/{author}/{repo}/{branch}/__inst__.py").content.decode("utf-8")
                    with open(f"{homePath}/pkg/cmd.py", "w") as initpy:
                        initpy.write(init)
                    
                    with open(homePath + "/data/addonsdef.json", "r") as temp1:
                        temp = json.load(temp1)

                    temp2 = data["cmd"]

                    with open(homePath + "/data/addonsdef.json", "w") as temp1:
                        temp.append(temp2)
                        temp1.write(json.dumps(temp))
                        
                    os.rename(f"{homePath}/pkg/cmd.py", f"{homePath}/addons/{temp2}.py")
                    
                    prg.increase(1)
                    prg.log(f"{c.Fore.GREEN}Successfully installed package!{c.Style.RESET_ALL}")
                except:
                    prg.log(f"{c.Fore.RED}Failed to install package!{c.Style.RESET_ALL}")
                finally:
                    prg.keyMode(False)
                    pass
            elif args[1] == "uninstall":
                noExec = True
                toExec = "rmv reg"
        elif args[0] == "ctest":
            get = "http://httpbin.org/get"
            post = "http://httpbin.org/post"

            if len(args) > 1:
                if len(args) == 2:
                    get = args[1]
                else:
                    get = args[1]
                    post = args[2]

            os.system(clearCmd)

            prg = f.progressBar("Testing Connection", 21, c.Fore.GREEN, c.Fore.LIGHTGREEN_EX, c.Fore.CYAN)
            prg.increase(1)
            prg.render()

            prg.increase(10)
            prg.setTitle("Testing Connection: GET")
            
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

                os.system(clearCmd)

                prg.render()

                print("Download\n" + get + "\n" + str(delta) + "\n" + c.Fore.GREEN + "Completed" + c.Style.RESET_ALL)

                temp3 = False
            else:

                os.system(clearCmd)
                prg.render()
                print("Download\n" + get + "\n#:##:##\n" + c.Fore.RED + "Failed" + c.Style.RESET_ALL)

                temp3 = True
            bt = str(datetime.datetime.now()).split(" ")[1]

            os.system(clearCmd)
            prg.setTitle("Testing Connection: POST")
            prg.render()

            prg.increase(10)
            prg.setTitle("Completed")

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

            os.system(clearCmd)

            if temp1:
                os.system(clearCmd)

                prg.render()
                print("Upload\n" + post + "\n" + str(delta) + "\n" + c.Fore.GREEN + "Completed" + c.Style.RESET_ALL)
            else:
                os.system(clearCmd)

                prg.render()
                print("Upload\n" + post + "\n#:##:##\n" + c.Fore.RED + "Failed" + c.Style.RESET_ALL)

            os.system(clearCmd)

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
            prg.keyMode(False)
        elif args[0] == "rmv":
            if args[1] == "reg":
                print("\n--- Registration Removal ---\n")
                prg = f.progressBar("Reading Command Data", 21, c.Fore.GREEN, c.Fore.LIGHTGREEN_EX, c.Fore.CYAN)
                prg.increase(1)
                prg.render()
                prg.increase(6)
                prg.setTitle("Reading addon dictionary")
                rmv = input("[string] Command to remove: ")
                f._upAndClear()
                f._upAndClear()
                f._upAndClear()
                prg.render()
                prg.increase(7)
                prg.setTitle("Editing addon dictionary")
                temp = open(homePath + "/data/addonsdef.json")
                temp1 = json.load(temp)
                temp.close()
                f._upAndClear()
                f._upAndClear()
                prg.render()
                prg.increase(6)
                prg.setTitle("Removing script file")
                os.remove(homePath + "/data/addonsdef.json")
                temp = open(homePath + "/data/addonsdef.json", "x")
                temp2 = []
                for v in temp1:
                    if v != rmv:
                        temp2.append(v)
                temp.write(json.dumps(temp2))
                temp.close()
                f._upAndClear()
                f._upAndClear()
                prg.render()
                prg.increase(1)
                prg.setTitle("Removed registration for " + rmv)
                if os.path.exists(homePath + "/addons/" + rmv + ".py"):
                    os.remove(homePath + "/addons/" + rmv + ".py")
                else:
                    raise Exception(f"{c.Fore.RED}Failed to delete addon script!{c.Style.RESET_ALL}")
                f._upAndClear()
                f._upAndClear()
                prg.render()
                prg.keyMode(False)
                os.system(clearCmd)
                print("\n--- Terminal + ---\n")
        elif args[0] == "clear":
            os.system(clearCmd)
        elif args[0] == "dev":
            if os.path.exists(f"{os.getenv("APPDATA")}/TerminalPlus/{ENVI}/DEV"):
                if args[1] == "commit" or args[1] == "push":
                    os.chdir(f"{homePath}/code")
                    os.rename(f"{homePath}/addons/addon-test.py", f"{homePath}/code/addon-test.py")
                    os.system("git add addon-test.py > ignore")
                    if os.system(f"git commit -a -m \"{"''".join(input("[string] Commit message: ").split("\""))}\" > ignore") == 0:
                        with open("ignore") as ign:
                            print(f.gitCommitBeautify(f.gitCommitParse(ign.read())))
                            if os.name == "nt":
                                try:
                                    input("Press [ENTER] to commit globally and [CTRL] + [Z], then [ENTER] to locally")
                                except EOFError:
                                    os.rename(f"{homePath}/code/addon-test.py", f"{homePath}/addons/addon-test.py")
                                    os.system("git commit -a -m \"Generated by T+ DEV: AUTO COMMIT\" > ignore")
                                    raise Exception("Local commit only")
                            if os.name == "posix":
                                try:
                                    input("Press [ENTER] to commit globally and [CTRL] + [D] to only commit locally")
                                except EOFError:
                                    os.rename(f"{homePath}/code/addon-test.py", f"{homePath}/addons/addon-test.py")
                                    os.system("git commit -a -m \"Generated by T+ DEV: AUTO COMMIT\" > ignore")
                                    raise Exception("Local commit only")
                            
                        if input("[true / false] force changes: ") == "true":
                            f._upAndClear()
                            print(f"[true / false] force changes: {c.Fore.GREEN}true\n{c.Fore.YELLOW}Forcing changes should only be done if you know what you're doing!{c.Style.RESET_ALL}")
                            if os.system("git push origin main --force > ignore") == 0:
                                print(f"{c.Fore.GREEN}Successfully pushed to main branch!{c.Style.RESET_ALL}")
                            else:
                                print(f"{c.Fore.RED}Failed to push changes!{c.Style.RESET_ALL}")
                        else:
                            f._upAndClear()
                            print(f"[true / false] force changes: {c.Fore.RED}false{c.Style.RESET_ALL}")
                            if os.system("git push origin main > ignore") == 0:
                                print(f"{c.Fore.GREEN}Successfully pushed to main branch!{c.Style.RESET_ALL}")
                            else:
                                print(f"{c.Fore.RED}Failed to push changes!{c.Style.RESET_ALL}")
                        os.rename(f"{homePath}/code/addon-test.py", f"{homePath}/addons/addon-test.py")
                        os.system("git commit -a -m \"Generated by T+ DEV: AUTO COMMIT\" > ignore")
                    else:
                        print(f"{c.Fore.RED}Failed to push changes!{c.Style.RESET_ALL}")
                        os.rename(f"{homePath}/code/addon-test.py", f"{homePath}/addons/addon-test.py")
                        os.system("git commit -a -m \"Generated by T+ DEV: AUTO COMMIT\" > ignore")
                    os.chdir(homePath)
                elif args[1] == "pull":
                    os.chdir(f"{homePath}/code")
                    if os.system("git pull > ignore") == 0:
                        with open("ignore") as ign:
                            if ign.read().find("Already up to date.") != -1:
                                print(f"{c.Fore.YELLOW}You're on the latest version already!{c.Style.RESET_ALL}")
                            else:
                                print(f"{c.Fore.GREEN}Successfully pulled main branch!{c.Style.RESET_ALL}\nChanges:")
                                print(f.gitCommitBeautify(f.gitCommitParse(ign.read())))
                    else:
                        print(f"{c.Fore.RED}Failed to pull changes!{c.Style.RESET_ALL}")
                    os.chdir(homePath)
                elif args[1] == "exit":
                    if os.system(f"rmdir {homePath}/code/.git /S /Q") == 0:
                        os.remove(f"{os.getenv("APPDATA")}/TerminalPlus/{ENVI}/DEV")
                        print(f"{c.Fore.GREEN}Successfully exited dev mode!{c.Style.RESET_ALL}")
                    else:
                        print(f"{c.Fore.RED}Failed to exit dev mode!{c.Style.RESET_ALL}")
                elif args[1] == "log":
                    os.chdir(f"{homePath}/code")
                    if os.system("git log --graph --pretty=\"{~%ad~}/~%s~/\" --date=human > ignore") == 0:
                        with open("ignore") as output:
                            out = []
                            for v in output.readlines():
                                if v.startswith("*") and f.extract(v, "* ", "|") == None and f.extract(v, "/~", "~/").removeprefix("~") != "Generated by T+ DEV: AUTO COMMIT":
                                    out.append({
                                        "msg": f.extract(v, "/~", "~/").removeprefix("~").replace("Generated by T+ DEV: ", f"{c.Fore.CYAN}DEV{c.Fore.LIGHTBLUE_EX} "),
                                        "date": f.extract(v, "{~", "~}").removeprefix("~")
                                    })
                            out.reverse()
                            for v in out:
                                print(f"{c.Fore.BLUE}{v["date"]} {c.Fore.LIGHTBLUE_EX}{v["msg"]}{c.Style.RESET_ALL}")
                    else:
                        print(f"{c.Fore.RED}Failed to get commits!{c.Style.RESET_ALL}")
                    os.chdir(homePath)
                elif args[1] == "store":
                    os.chdir(f"{homePath}/code")
                    if args[2] == "list":
                        if os.system("git stash list --oneline > ignore") == 0:
                            with open("ignore") as ign:
                                stashes = f.gitStashParse(ign.read())
                                for v in stashes:
                                    print(f"{c.Fore.LIGHTBLUE_EX}{v["hash"]} {c.Fore.BLUE}{v["comment"]}{c.Style.RESET_ALL}")
                        else:
                            print(f"{c.Fore.RED}Failed to gather store!{c.Style.RESET_ALL}")
                    os.chdir(homePath)
            else:
                print(f"{c.Fore.RED}This installation is not a development one!{c.Style.RESET_ALL}")
        elif args[0] == "log":
            if args[1] == "read":
                temp = open(homePath + "/data/termP.log")
                temp1 = temp.read()
                temp.close()
                temp1 = str(c.Fore.RED + "FATAL" + c.Style.RESET_ALL).join(temp1.split("FATAL"))
                temp1 = str(c.Fore.YELLOW + "ERROR" + c.Style.RESET_ALL).join(temp1.split("ERROR"))
                temp1 = str(c.Fore.BLUE + "INFO" + c.Style.RESET_ALL).join(temp1.split("INFO"))
                temp1 = str(c.Fore.GREEN + "STARTUP" + c.Style.RESET_ALL).join(temp1.split("STARTUP"))
                print("\n--- Logs ---\n")
                print(temp1)
                print(f"Log Size: {c.Fore.YELLOW}" + str(round(os.stat(homePath + "/data/termP.log").st_size / (1024 * 1024), 2)) + f" MiB{c.Style.RESET_ALL}")
                print("\n--- Terminal + ---\n")
            elif args[1] == "write":
                log("[" + args[2] + "] " + str(" ").join(args[3:len(args) - 1]), args[len(args) - 1])
            elif args[1] == "clear":
                print("Cleared the logs")
                clearLog()
        elif args[0] == "inst":
            if args[1] == "new":
                if f.selPrompt(["Yes", "No"], [">", "<"], "Are you sure you would like to setup a new installation?") == 0:
                    runpy.run_path(homePath + "/code/newEnv.py")
                print("\n--- Terminal + ---\n")
            elif args[1] == "open":
                inst = input("[string] (Leave blank to open with directory) Installation name to open: ")
                if inst == "":
                    inst = input("[directory] Installation directory to open: ")
                else:
                    if os.path.exists(os.getenv("AppData") + "/TerminalPlus/" + inst + "/PATH"):
                        temp = open(os.getenv("AppData") + "/TerminalPlus/" + inst + "/PATH")
                        inst = temp.read()
                        temp.close()
                    else:
                        print(f"{c.Fore.RED} Invalid Installation")
                
                os.system(f"python \"{inst}\"/code")
            elif args[1] == "del":
                if f.selPrompt([c.Fore.YELLOW + "Yes" + c.Style.RESET_ALL, "No"], ["!", "<"], "Are you sure you want to delete an installation?") == 0:
                    print(c.Fore.BLUE + "Hint: MAIN is the installation that starts up and is installed by default." + c.Style.RESET_ALL)
                    inst = input("[string] Installation name to delete: ")
                    temp = open(os.getenv("AppData") + "/TerminalPlus/" + inst + "/PATH")
                    instN = inst
                    inst = temp.read()
                    temp.close()
                    if f.selPrompt([c.Fore.RED + "Yes" + c.Style.RESET_ALL, "No"], ["!", "<"], "Are you really sure you want to delete the installation: " + instN + "?") == 0:
                        print("Enter the installation name to delete.\n" + c.Fore.BLUE + "Deleting an installation means that ALL files in the installation folder are deleted!" + c.Style.RESET_ALL)
                        print(c.Fore.CYAN + "Installation Name: " + instN + "\nInstallation Folder: " + inst + c.Style.RESET_ALL)
                        if input("3: ") != instN:
                            if input("2: ") != instN:
                                if input("1: ") != instN:
                                    raise Exception(f"{c.Fore.RED}User failed to enter installation name.{c.Style.RESET_ALL}")
                        os.system("rmdir \"" + inst + "\" /S /Q")
                        os.system("rmdir " + os.getenv("AppData") + "\"/TerminalPlus/" + instN + "\" /S /Q")
                        os.system(clearCmd)
                        print(f"Removed Installation {instN}")
            elif args[1] == "list":
                temp = g.glob(os.path.join(os.getenv("AppData"), "TerminalPlus", "*"))
                print("\n--- All Installations ---\n")

                for v in temp:
                    if v.removeprefix(os.path.join(os.getenv("AppData"), "TerminalPlus")).find("/") == -1 and os.path.isdir(v) and v.removeprefix(os.path.join(os.getenv("AppData"), "TerminalPlus")) != "SYS-RES":
                        temp1 = open(v + "/PATH")
                        temp2 = temp1.read()
                        temp1.close()
                        if v == os.path.join(os.getenv("AppData"), "TerminalPlus", "MAIN"):
                            print(f"{c.Fore.GREEN}DEF{c.Style.RESET_ALL} [ENV] {v.removeprefix(os.path.join(os.getenv("AppData"), "TerminalPlus") + os.path.sep)} {temp2}")
                        elif os.path.exists(f"{v}/DEV"):
                            print(f"{c.Fore.BLUE}DEV{c.Style.RESET_ALL} [ENV] {v.removeprefix(os.path.join(os.getenv("AppData"), "TerminalPlus") + os.path.sep)} {temp2}")
                        else:
                            print(f"{c.Fore.YELLOW}STD{c.Style.RESET_ALL} [ENV] {v.removeprefix(os.path.join(os.getenv("AppData"), "TerminalPlus") + os.path.sep)} {temp2}")
                print("\n--- Terminal + ---\n")
        else:
            found = False
            temp = open(homePath + "/data/addonsdef.json")

            temp1 = json.load(temp)

            for i in range(len(temp1)):
                if temp1[i] == args[0]:
                    found = True
                    temp.close()
                    temp = None
                    break
            
            if found:
                temp = open(homePath + "/data/args.json", "w")
                temp.write(json.dumps(args))
                temp.close()

                runpy.run_path(homePath + "/addons/" + args[0] + ".py")
            else:
                print("Unknown command: " + args[0] + "\nIf this is an addon command, you can install it with the command reg\nIf you have already installed it, use rmv reg " + args[0] + " and then reg again.")

    except Exception as ex:
        template = "ERR\nTYP: {0}\nARG: {1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        log("Exception: " + type(ex).__name__ + " {0!r}".format(ex.args), "ERROR")
    finally:
        pass

if not cliExec:
    os.system(clearCmd)
