

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import shutil
import schedule
import time

import GUI_main


def center_window(self, w, h): #PASS IN TKINTER FRAME (MASTER REFERENCE AND THE W AND H
    screen_width = self.master.winfo_screenwidth() #Get screen width
    screen_height = self.master.winfo_screenheight() #Get screen height
    x = int((screen_width/2) - (w/2))#Calc X coordinate CALCULATE X AND Y COORDINATES TO PAINT THE APP CENTERED ON THE USER'S SCREEN
    y = int((screen_height/2) - (h/2))#Calc Y coordinate 
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #CLOSE GUI
        self.master.destroy()
        os._exit(0)


def browse1():
    folder_path1
    dirname1 = filedialog.askdirectory()
    folder_path1.set(dirname1)
    #return dirname1


def browse2():
    folder_path2
    dirname2 = filedialog.askdirectory()
    folder_path2.set(dirname2)
    #return dirname2 


##def copy_files():
##    working = folder_path1.get() + "/"
##    copies = folder_path2.get() + "/"
##    for files in os.listdir(working):
##        shutil.copy2(working +files, copies +files)
##        if (not os.path.exists(copies)) or (os.stat(working).st_mtime - os.stat(copies).st_mtime > 0):
##            shutil.copy2(working +files, copies +files)

if __name__ == "__main__":
    folder_path1=StringVar()
    folder_path2=StringVar()
