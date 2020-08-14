#   PYTHON COURSE
#   ASSIGNMENT: SCRIPT GUI CHALLENGE
#   AUTHOR: KIRK HILTON


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import shutil
import schedule
import time

import GUI_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #CREATE MASTER FRAME WINDOW
        self.master = master
        self.master.minsize(550,175)
        self.master.maxsize(550,175)

        #CENTER THE WINDOW
        center_window(self,550,175)

        #ADD TITLE AND BACKGROUND COLOR
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        #GUI BUTTONS
        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text="Source dir...",command = lambda: browse1())
        self.btn_browse1.grid(row=2,column=0,padx=(15,0),pady=(40,0),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12,height=1,text="Destination...",command = lambda: browse2())
        self.btn_browse2.grid(row=3,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_checkForFiles = tk.Button(self.master,width=12,height=2,text="Check for files...",command = lambda: copy_files())
        self.btn_checkForFiles.grid(row=4,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=12,height=2,text="Close Program",command = lambda: ask_quit(self))
        self.btn_close.grid(row=4,column=1,padx=(15,0),pady=(10,0),sticky=S+E)
        
        #GUI TEXT BOXES
        self.txt_browse1 = tk.Entry(self.master,width=65,text = folder_path1)
        self.txt_browse1.grid(row=2,column=1,padx=(25,0),pady=(35,0),sticky=W)
        self.txt_browse2 = tk.Entry(self.master,width=65,text = folder_path2)
        self.txt_browse2.grid(row=3,column=1,padx=(25,0),pady=(5,0),sticky=W)

        #CATCH IF USER CLICKS 'X' TO CLOSE WINDOW
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master





##def scheduled_check():
##    #filedialog.SEL_LAST
##    working = filedialog.askdirectory(initialdir) + "/"
##    copies = filedialog.askdirectory(initialdir) + "/"
##    for files in os.listdir(working):
##        shutil.copy2(working +files, copies +files)
##        if (not os.path.exists(copies)) or (os.stat(working).st_mtime - os.stat(copies).st_mtime > 0):
##            shutil.copy2(working +files, copies +files)
##    
##    schedule.every().day.at('02:00').do(scheduled_check)
##    while 1:
##        schedule.run_pending()
##        time.sleep(1)

##try:
##    x=filedialog.askdirectory(initialdir=open('.my_script_lastdir').read())
##except:
##    x=filedialog.askdirectory()
##with open('.my_script_lastdir', 'w') as f: f.write(x)
##
##print(x)


if __name__ == "__main__":
    root = tk.Tk()
    folder_path1=StringVar()
    folder_path2=StringVar()
    App = ParentWindow(root)
    #scheduled_check()
    root.mainloop()


#working = filedialog.SEL_LAST
#copies = fildialog.SEL_LAST    
#Set the destination path
#Set the location of the source files
