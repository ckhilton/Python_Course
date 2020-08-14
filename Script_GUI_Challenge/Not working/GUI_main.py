#   PYTHON COURSE
#   ASSIGNMENT: SCRIPT GUI CHALLENGE
#   AUTHOR: KIRK HILTON

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#import GUI_func
#import GUI


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550,175)
        self.master.maxsize(550,175)
        #CENTER WINDOW
        GUI_func.center_window(self,550,200)
        
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        #CATCH USER CLICK 'X' TO CLOSE WINDOW
        self.master.protocol("WM_DELETE_WINDOW", lambda: GUI_func.ask_quit(self))
        arg = self.master

        #GUI.load_gui(self)

root=tk.Tk()    

ent1=tk.Entry(root,font=40)
ent1.grid(row=2,column=2)

def browsefunc():
    filename =tkFileDialog.askopenfilename(filetypes=(("tiff files","*.tiff"),("All files","*.*")))
    ent1.insert(tk.END, filename) # add this
       


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
