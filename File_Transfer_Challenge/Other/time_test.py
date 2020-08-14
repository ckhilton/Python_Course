
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from os import *
import os
import platform
import glob
import shutil
import schedule
import time
import datetime



path = os.getcwd()
path = os.chdir("Working_Files")


#'C:Users/Student/Desktop/myProjects/Python_Course/File_Transfer_Challenge/Working_Files/'

for files in os.listdir(path):
    if files[-4:]=='.txt':
        print(datetime.datetime.fromtimestamp(os.path.getctime(files)))
        print(datetime.datetime.fromtimestamp(os.path.getmtime(files)))
