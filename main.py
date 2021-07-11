#!/usr/bin/python
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
import time
from tkinter import font
# Startup
from tkinter import *

master = tk.Tk()
master.title("YOS 2 Developer Alpha")
master.iconbitmap
master.geometry("500x600")

import os
import ctypes

if not os.path.isdir("C://Program Files"):

    directory = "YOS2"
    parent_dir = "C://Program Files"
    directory2 = "YDocs"
    parentdir2 = "C://Program Files/YOS2"
    directory3 = "SetupFiles"
    parentdir3 = "C://Program Files/YOS2"
    import os
    path = os.path.join(parent_dir, directory)

    os.makedirs(path)
else:
    print("")
import time


# Functions
def ydocs():
    ydocswindow = Tk()
    ydocswindow.title("YDocs 2 Developer Alpha")
    statusBar = Label(ydocswindow, text="Ready     ")
    frame = Frame(ydocswindow)
    frame.pack(pady=5)
    text_scroll = Scrollbar(frame)
    text_scroll.pack(side=RIGHT, fill=Y)
    text = Text(frame, width=97, height=25, font=("Helvetica", 16), selectbackground="dark blue",
                selectforeground="white",
                undo=True, yscrollcommand=text_scroll.set)

    def newFile():
        text.delete("1.0", END)

    def ydocsinfo():
        ydocsinfowindow = Tk()
        ydocsinfowindow.title("About YDocs")
        YDOCSITTLE = Label(ydocsinfowindow, text="YDocs 2.0 Public Alpha", font=("Bold", 25))
        YDOCSFROMVERSION = Label(ydocsinfowindow, text="Comes With YOS Alander", font=("Italic", 18))
        YDOCSITTLE.pack()
        YDOCSFROMVERSION.pack()
    menu = Menu(ydocswindow)
    ydocswindow.config(menu=menu)
    # Add file menu
    file_menu = Menu(menu)
    menu.add_cascade(label="YDocs", menu=file_menu)
    file_menu.add_command(label="About YDocs", command=ydocsinfo)
    file_menu.add_separator()
    file_menu.add_command(label="New", command=newFile)
    file_menu.add_separator()
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Exit")
    text.pack()
    text_scroll.config()
    dir = os.path.join("C://", "temp", "python")
    if not os.path.exists(dir):
        os.mkdir(dir)


# Code to add widgets will go here...

fsw = tk.Label(
    text="This is a developer test Alpha release. CONFIDENTIAL.",
    height=2,

)
yosnote = tk.Label(text="YOS 2")
appLButton = tk.Button(
    master,
    text="YDocs 2 Public Alpha 1",
    command=ydocs
)


# Packing
yosnote.pack()
fsw.pack()
appLButton.pack()
master.mainloop()

