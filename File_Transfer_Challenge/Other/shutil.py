#   PYTHON COURSE
#   ASSIGNMENT: STEP 230
#   AUTHOR: KIRK HILTON

import shutil
import os

def moveFiles():
    #Set the location of the source files
    source = '/Users/Student/Desktop/Folder A/'
    #Set the destination path
    destination = '/Users/Student/Desktop/Folder B/'
    files = os.listdir(source)

    for i in files:
        #Use 'i' to move files to new destination
        shutil.move(source+i, destination)


if __name__ == "__main__":
    moveFiles()
    
