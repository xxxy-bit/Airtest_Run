import os
from tkinter import *
from tkinter import filedialog

def choose_path():
    cp = filedialog.askdirectory()
    path.set(cp)

# os.system("start explorer G:\tester\jpg")
master = Tk()
path = StringVar()


Entry(master, textvariable=path).grid(row=0, column=0)
Button(master, text='选择路径', command=choose_path).grid(row=0, column=1)

master.mainloop()