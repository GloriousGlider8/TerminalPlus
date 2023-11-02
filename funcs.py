import keyboard as k
import os
import time
import colorama as c

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
LINE_UC = LINE_UP + LINE_CLEAR

def upAndClear() -> None:
    print(LINE_UP, end=LINE_CLEAR)

def isFlot(test: any) -> bool:
	if test.find(".") == 1:
		split = str(test).split(".")
		if split[0].isnumeric() and split[1].isnumeric():
			return True

def isNega(test: any) -> bool:
	if test.startswith("-"):
		if test.removeprefix("-").isnumeric():
			return True

def selPrompt(options: list, icons: list, intro: str) -> int:
    os.system("cls")
    print(intro)
    print("\nUse [↑] and [↓] to move cursor.\nUse [→] to select.\n")

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

def stringSelect(intro: str, default: str, numReq: bool, intReq: bool, fltReq: bool, posReq: bool, negReq: bool, maxChar: int, minChar: int) -> str:
    os.system("cls")
    print(intro)
    print("Use [←] to edit the text.\nOnce you have finished, use [→].")

    sel = default
    targets = 0
    isNum = False
    isInt = False
    isFlt = False
    isPos = False
    isNeg = False
    isMax = False
    isMin = False
    print(c.Fore.BLUE + sel + c.Style.RESET_ALL)
    
    if numReq:
        print(c.Fore.YELLOW + "[→] Must be a number." + c.Style.RESET_ALL)
        targets = targets + 1
    if intReq:
        print(c.Fore.YELLOW + "[→] Number must be whole." + c.Style.RESET_ALL)
        targets = targets + 1
    if fltReq:
        print(c.Fore.YELLOW + "[→] Number must have a decimal point." + c.Style.RESET_ALL)
        targets = targets + 1
    if posReq:
        print(c.Fore.YELLOW + "[→] Number must be positive." + c.Style.RESET_ALL)
        targets = targets + 1
    if negReq:
        print(c.Fore.YELLOW + "[→] Number must be negative." + c.Style.RESET_ALL)
        targets = targets + 1
    if maxChar != -1:
        print(c.Fore.YELLOW + "[→] Must be less than " + str(maxChar) + " characters." + c.Style.RESET_ALL)
        targets = targets + 1
    if minChar != -1:
        print(c.Fore.YELLOW + "[→] Must be at least " + str(minChar) + " characters." + c.Style.RESET_ALL)
        targets = targets + 1

    while True:
        time.sleep(0.15)
        
        for _ in range(targets):
           upAndClear()

        if numReq and sel.isnumeric():
            print(c.Fore.GREEN + "[ ] Input is a number." + c.Style.RESET_ALL)
            isNum = True
        elif numReq and isFlot(sel):
            print(c.Fore.GREEN + "[ ] Input is a number." + c.Style.RESET_ALL)
            isNum = True
        elif numReq and isNega(sel):
            print(c.Fore.GREEN + "[ ] Input is a number." + c.Style.RESET_ALL)
            isNum = True
        elif numReq:
            print(c.Fore.YELLOW + "[→] Must be a number." + c.Style.RESET_ALL)
            isNum = False
        else:
            isNum = True
        
        if intReq and sel.find(".") == -1 and sel.isnumeric():
            print(c.Fore.GREEN + "[ ] Input is whole." + c.Style.RESET_ALL)
            isInt = True
        elif intReq:
            print(c.Fore.YELLOW + "[→] Number must be whole." + c.Style.RESET_ALL)
            isInt = False
        else:
            isInt = True

        if fltReq and isFlot(sel):
            print(c.Fore.GREEN + "[ ] Input has a decimal point." + c.Style.RESET_ALL)
            isFlt = True
        elif fltReq:
            print(c.Fore.YELLOW + "[→] Number must have a decimal point." + c.Style.RESET_ALL)
            isFlt = False
        else:
            isFlt = True

        if posReq and sel.isnumeric() and float(sel) > -1:
            print(c.Fore.GREEN + "[ ] Input is positive." + c.Style.RESET_ALL)
            isPos = True
        elif posReq:
            print(c.Fore.YELLOW + "[→] Number must be positive." + c.Style.RESET_ALL)
            isPos = False
        else:
            isPos = True
        
        if negReq and isNega(sel):
            print(c.Fore.GREEN + "[ ] Input is negative." + c.Style.RESET_ALL)
            isNeg = True
        elif negReq:
            print(c.Fore.YELLOW + "[→] Number must be negative." + c.Style.RESET_ALL)
            isNeg = False
        else:
            isNeg = True
        
        if maxChar != -1 and len(sel) <= maxChar:
            print(c.Fore.GREEN + "[ ] Input is less than " + str(maxChar) + " characters." + c.Style.RESET_ALL)
            isMax = True
        elif maxChar != -1:
            print(c.Fore.YELLOW + "[→] Must be less than " + str(maxChar) + " characters." + c.Style.RESET_ALL)
            isMax = False
        else:
            isMax = True
        
        if minChar != -1 and len(sel) >= minChar:
            print(c.Fore.GREEN + "[ ] Input is at least " + str(minChar) + " characters." + c.Style.RESET_ALL)
            isMin = True
        elif minChar != -1:
            print(c.Fore.YELLOW + "[→] Must be at least " + str(minChar) + " characters." + c.Style.RESET_ALL)
            isMin = False
        else:
            isMin = True
        
        if k.is_pressed("left"):
            os.system("cls")
            print("Old Input: " + sel)
            print(c.Fore.BLUE + "Hint: Use [↑] to retype the last input." + c.Style.RESET_ALL + "\nUse [→] to retype it one character at a time.\nUse [ENTER] when you are finished.")
            sel = input(c.Fore.CYAN + "New Input: ")
            print("", end=c.Style.RESET_ALL)
            os.system("cls")
            print(intro)
            print("Use [←] to edit the text.\nOnce you have finished, use [→].")
            print(c.Fore.BLUE + sel + c.Style.RESET_ALL)
            for _ in range(targets):
                print()
        
        if k.is_pressed("right"):
            if isNum and isInt and isFlt and isPos and isNeg and isMax and isMin:
                os.system("cls")
                return sel
            else:
                input(c.Fore.RED + "Check the requirements first!" + c.Style.RESET_ALL + "\nPress [ENTER] to continue...")
                upAndClear()
                upAndClear()

def fltList(listEdt: list, item: any) -> list:
    res = list(filter((item).__ne__, listEdt)) 
    return res

class progressBar:
    def __init__(self, title: str, max: int):
        self.prg = 0
        self.title = title
        self.max = max

    def increase(self, amount: int) -> None:
        self.prg += amount
    
    def decrease(self, amount: int) -> None:
        self.prg -= amount
    
    def setTitle(self, title: str) -> None:
        self.title = title
    
    def render(self) -> None:
        num = self.prg / self.max
        decimal = num * 100
        per = round(decimal, 2)
        print(self.title)
        print("", end=" ")
        for _ in range(self.prg):
            print(c.Fore.LIGHTGREEN_EX + "█", end=c.Style.RESET_ALL)
        for _ in range(self.max - self.prg):
            print(c.Fore.GREEN + "█", end=c.Style.RESET_ALL)
        print(" " + str(per) + "%")

#def selExplore(data: str):
#    temp = []
#    temp1 = []
#    with open(data, "r") as openD:
#        with openD.readlines() as rawdata:
#            for i, v in enumerate(rawdata):
#                if v.startswith("#"):
#                    temp.append(v.removeprefix("#"))
#                    temp1.append("__END__")
#                else:
#                    temp1.append(v)
#    
#    temp2 = []
