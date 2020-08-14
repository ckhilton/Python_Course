#   PYTHON COURSE
#   ASSIGNMENT: FILE TRANSFER ASSIGNMENT PART TWO
#   AUTHOR: KIRK HILTON

import os
import shutil
import schedule
import time

def copy_files():
    #Set the location of the source files
    working = "/Users/Student/Desktop/myProjects/Python_Course/File_Transfer_Challenge/Working_Files/"
    #Set the destination path
    copies = "/Users/Student/Desktop/myProjects/Python_Course/File_Transfer_Challenge/Copies/"

    for files in os.listdir(working):
        shutil.copy2(working +files, copies +files)
        if (not os.path.exists(copies)) or (os.stat(working).st_mtime - os.stat(copies).st_mtime > 1):
            shutil.copy2(working +files, copies +files)

def move_files():
    #Set the location of the source files
    copies = "/Users/Student/Desktop/myProjects/Python_Course/File_Transfer_Challenge/Copies/"
    #Set the destination path
    home_office = "/Users/Student/Desktop/myProjects/Python_Course/File_Transfer_Challenge/Home_Office/"

    for files in os.listdir(copies):
        #Use 'i' to move files to new destination
        shutil.move(copies +files, home_office +files)


def scheduler():
    schedule.every().day.at('17:00').do(copy_files)
    schedule.every().day.at('00:00').do(move_files)
    
    while 1:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    copy_files()
    move_files()
    scheduler()


    
