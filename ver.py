from tkinter import ttk
from tkinter import font
import tkinter as tk
import os

def ver(cmd):
    global __input__

    base = tk.Tk()

    base.title("Dangerous Action!")

    text1 = ttk.Label(base, text="The command you are going to execute may harm your computer!\nTo confirm execution, type A1B2C3 in the box below.")

    text1.grid(padx=30, pady=30, row=1, column=1)

    text2 = ttk.Label(base, text=str(cmd), font=("Calibri", 16), foreground="#FF0000")

    text2.grid(padx=30, pady=20, row=2, column=1)

    __input__ = ttk.Entry(base)

    __input__.grid(padx=30, pady=10, row=3, column=1)

    base.mainloop()

ver("kill windows.exe")