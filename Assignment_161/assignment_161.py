import os
import time


   
def findTxt():
    path = os.getcwd()
    fileList = os.listdir(path)
    for f in fileList:
        if f.endswith(".txt"):
            full = os.path.join(path,f)
            time = os.path.getmtime(full)
            #local = time.ctime(time)
            print(f,time)
     
        
if __name__ == "__main__":
    findTxt()
   



