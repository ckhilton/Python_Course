import os
import time



def findTxt():
    path = os.getcwd()
    fileList = [os.path.join(path,f)for f in os.listdir(path) if f.endswith(".txt")]
    for f in fileList:
        time = os.path.getmtime(f)
        print(f,time)

        
if __name__ == "__main__":
    findTxt()
   



