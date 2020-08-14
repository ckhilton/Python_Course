

import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk

import GUI_main
import GUI

def center_window(self, w, h): #PASS IN THE TKINTER FRAME (MASTER REFERENCE AND THE W AND H
    #GET THE USERS SCREEN WIDTH AND HEIGHT
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #CALCULATE X AND Y COORDINATES TO PAINT THE APP CENTERED ON THE USER'S SCREEN
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #THIS CLOSES THE APP
        self.master.destroy()
        os._exit(0)

def askdirectory(self):
    dirname = filedialog.askdirectory()
    if dirname:
        var.set(dirname)

def UserFileInput(self,status,name):
    optionFrame = Frame(master)
    optionLabel = Entry(optionFrame)
    optionLabel["text"] = self.name
    #optionLabel.pack(side=LEFT)
    text = self.status
    var = StringVar(master)
    var.set(text)
    w = Entry(optionFrame, textvariable= var)
    #w.pack(side = LEFT)
    optionFrame.pack()
    return self.w, self.var


if __name__ == "__main__":
    pass

