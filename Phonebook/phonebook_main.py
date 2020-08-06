#   PYTHON COURSE:  PYTHON VERSION 3.8.3
#   ASSIGNMENT:     PHONEBOOK
#   AUTHOR:         KIRK HILTON
#   PURPOSE:        CREATE A PHONEBOOK WITH OOP, TKINTER GUI MODULE,
#                   AND USE OF TKINTER PARENT AND CHILD RELATIONSHIPS.

#   TEST:           WRITTEN AND TESTED TO WORK WITH WINDOWS 10 PRO
#                   (VERSION 10.0.18363 BUILD 18363)

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#BE SURE TO IMPORT THE OTHER MODULES SO WE
#CAN HAVE ACCESS TO THEM (CREATED LATER)
import phonebook_gui
import phonebook_func

#Frame IS THE TKINTER CLASS THAT OUR OWN CLASS ParentWindow() 
#WILL INHERIT PROPERTIES AND METHODS FROM
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #DEFINE OUR MASTER FRAME CONFIGURATION
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        #THIS CenterWindow METHOD WILL CENTER THE APP ON THE USER'S SCREEN
        phonebook_func.center_window(self,500,300)
        self.master.title("Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")
        #THIS PROTOCOL METHOD IS A TKINTER BUILD-IN METHOD TO CATCH IF THE
        #USER CLICKS THE UPPER CORNER, "X" ON WINDOWS OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #LOAD IN THE GUI WIDGETS FROM A SEPARATE MODULE, KEEPING
        #YOUR CODE COMPARTMENTALIZED AND CLUTTER-FREE
        phonebook_gui.load_gui(self)

        #INSTANTIATE THE TKINTER MENU DROPDOWN OBJECT
        #THIS IS THE MENU THAT WILL APPEAR AT THE TOP OF CUR WINDOW
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) # defines the particular drop down colum and tearoff=0 means do not separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo") # add_command is a child menubar item of the add_cascde parent item
        menubar.add_cascade(label="Help", menu=helpmenu) # add_cascade is a parent menubar item (visible heading)
        """
            Finally, we apply the config method of the widget to display the menu
            From here we could also pass in additional aprams for additional 
            functionalityor appearances such as a borderwidth.
        """
        self.master.config(menu=menubar, borderwidth='1')

        
"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""


if __name__ == "__main__": #CONTROL
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
