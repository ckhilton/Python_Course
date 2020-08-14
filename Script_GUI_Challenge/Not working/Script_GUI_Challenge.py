#   PYTHON COURSE
#   ASSIGNMENT: SCRIPT GUI CHALLENGE
#   AUTHOR: KIRK HILTON

from tkinter import *
import tkinter as tk
from tkinter import messagebox

import GUI_func
import GUI


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(525,175)
        self.master.maxsize(525,175)
        #CENTER WINDOW
        GUI_func.center_window(self,700,300)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        #CATCH USER CLICK 'X' TO CLOSE WINDOW
        self.master.protocol("WM_DELETE_WINDOW", lambda: GUI_func.ask_quit(self))
        arg = self.master
        
        GUI.load_gui(self)
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    #w, var = UserFileInput("", "")
    root.mainloop()
    
