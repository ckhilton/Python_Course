#   PYTHON COURSE
#   ASSIGNMENT: SCRIPT GUI CHALLENGE
#   AUTHOR: KIRK HILTON

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(550,175)
        self.master.maxsize(550,175)

        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

"""def load_gui(self):

    #DEFINE BUTTONS
    self.btn_Browse1 = tk.Button(self.master,width=12,height=1,text="Browse...",command = lambda: GUI_func.askdirectory(self))
    self.btn_Browse1 = tk.Button(self.root,width=12,height=1,text='Browse...', command = lambda: GUI_func.askdirectory(self))
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
    self.btn_Browse1.grid(side=LEFT)
    self.txt_Browse2 = tk.Entry(self.master,width=65,text="")
    self.txt_Browse2.grid(row=3,column=1,padx=(25,0),pady=(5,0),sticky=W)

    self.btn_Browse1 = Button(self.master, text="Browse...",command = lambda: GUI_func.UserFileInput(self,"",""))
    self.btn_Browse1.pack(side = LEFT)

    self.w, self.var = UserFileInput("", "")"""

from tkinter import *
import tkinter as tk
import filedialog

root=tk.Tk()    

ent1=tk.Entry(root,font=40)
ent1.grid(row=2,column=2)

def browsefunc():
    filename =tkFileDialog.askopenfilename(filetypes=(("tiff files","*.tiff"),("All files","*.*")))
    ent1.insert(tk.END, filename) # add this

b1=tk.Button(root,text="DEM",font=40,command=browsefunc)
b1.grid(row=2,column=4)

root.mainloop()
