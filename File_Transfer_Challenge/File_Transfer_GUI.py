#   PYTHON VERSION 3.8.3
#   ASSIGNMENT: FILE TRANSFER GUI CHALLENGE
#   AUTHOR: KIRK HILTON


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from os import *
import os
import shutil
import schedule
import time
import datetime



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #CREATE MASTER FRAME WINDOW
        self.master = master
        self.master.minsize(575,175)
        self.master.maxsize(557,175)

        #CENTER THE WINDOW
        center_window(self,550,175)

        #ADD TITLE AND BACKGROUND COLOR
        self.master.title("Source Directory/File Destination (24hr check for updates w/ file transfer)")
        self.master.configure(bg="#F0F0F0")

        #GUI BUTTONS
        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text="Source...",command = lambda: browse1())
        self.btn_browse1.grid(row=2,column=0,padx=(15,0),pady=(40,0),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text="Destination...",command = lambda: browse2())
        self.btn_browse2.grid(row=3,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_checkForFiles = tk.Button(self.master,width=15,height=2,text="Check/Transfer...",command = lambda: copy_files())
        self.btn_checkForFiles.grid(row=4,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text="Close Program",command = lambda: ask_quit(self))
        self.btn_close.grid(row=4,column=1,padx=(15,0),pady=(10,0),sticky=S+E)
        
        #GUI TEXT BOXES
        self.txt_browse1 = tk.Entry(self.master,width=65,text = folder_path1)
        self.txt_browse1.grid(row=2,column=1,padx=(25,0),pady=(35,0),sticky=W)
        self.txt_browse2 = tk.Entry(self.master,width=65,text = folder_path2)
        self.txt_browse2.grid(row=3,column=1,padx=(25,0),pady=(5,0),sticky=W)

        #CATCH IF USER CLICKS 'X' TO CLOSE WINDOW
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master

            
def center_window(self, w, h): #PASS IN TKINTER FRAME (MASTER REFERENCE AND THE W AND H
    screen_width = self.master.winfo_screenwidth() #Get screen width
    screen_height = self.master.winfo_screenheight() #Get screen height
    x = int((screen_width/2) - (w/2))#Calc X coordinate CALCULATE X AND Y COORDINATES TO PAINT THE APP CENTERED ON THE USER'S SCREEN
    y = int((screen_height/2) - (h/2))#Calc Y coordinate 
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


def ask_quit(self): #ASK IF OK TO CLOSE GUI
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()


def browse1(): #1st function for command in 'btn_browse1' to browse for a source directory
    folder_path1
    global dir_path1 
    dir_path1 = filedialog.askdirectory()
    folder_path1.set(dir_path1)


def browse2(): #2nd function for command in 'btn_browse2' to browse for a destination to copy any modified files
    folder_path2
    global dir_path2
    dir_path2 = filedialog.askdirectory()
    folder_path2.set(dir_path2)


def copy_files():
    time_now = datetime.datetime.now() #Get current local time
    tdelta = datetime.timedelta(hours=24) #<timedelta> will set window of time (named 'tdelta' here for a 24 hour window).
    day_ago = time_now - tdelta #Get time from 24 hours ago relative to 'time_now'
    global abs_path1
    global abs_path2
    for src_files in os.listdir(dir_path1):
        if src_files.endswith('.txt'): #GET TEXT FILES ONLY
            abs_path1 = os.path.join(dir_path1, src_files)
            file_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(abs_path1))
        if file_modified_time < day_ago: #COMPARE FILE MODIFICATION TIMES
            shutil.copy2(abs_path1, dir_path2) #TRANSFER FILES IF MODIFIED/CREATED LESS THAN 24 HOURS AGO
    messagebox.showinfo("Alert","Source files created or modified\nwithin the last 24 hours have now been\ncopied/updated to the destination folder!")
        # else file_modified_time > day_ago:

         
if __name__ == "__main__": #CONTROL
    root = tk.Tk()
    folder_path1=StringVar()
    folder_path2=StringVar()
    App = ParentWindow(root)
    root.mainloop()
