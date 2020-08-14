

from tkinter import *
import tkinter as tk

#BE SURE TO IMPORT OUR OTHER MODULES
#SO WE CAN HAVE ACCESS TO THEM
import GUI_func
import GUI_main

def load_gui(self):

    #DEFINE BUTTONS
    self.btn_Browse1 = tk.Button(self.master,width=12,height=1,text="Browse...",command=lambda: GUI_func.askdirectory(self))
    self.btn_Browse1.grid(row=2,column=0,padx=(15,0),pady=(40,0),sticky=W)
    self.btn_Browse2 = tk.Button(self.master,width=12,height=1,text="Browse...")
    self.btn_Browse2.grid(row=3,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_Check = tk.Button(self.master,width=12,height=2,text="Check for files...")
    self.btn_Check.grid(row=4,column=0,padx=(15,0),pady=(10,0),sticky=W)
    self.btn_Close = tk.Button(self.master,width=12,height=2,text="Close Program",command=lambda: GUI_func.ask_quit(self))
    self.btn_Close.grid(row=4,column=1,padx=(15,0),pady=(10,0),sticky=S+E)
    
    #DEFINE TEXT BOXES
    self.txt_Browse1 = tk.Entry(self.master,width=65,text="")
    self.txt_Browse1.grid(row=2,column=1,padx=(25,0),pady=(35,0),sticky=W)
    self.txt_Browse2 = tk.Entry(self.master,width=65,text="")
    self.txt_Browse2.grid(row=3,column=1,padx=(25,0),pady=(5,0),sticky=W)


if __name__ == "__main__":
    pass
