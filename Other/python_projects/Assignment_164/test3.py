#   ASSIGNMENT: STEP 164
#   AUTHOR: KIRK HILTON


import sqlite3
import os

def assignment(): #define the function
    conn = sqlite3.connect("Assignment_164.db") #connect to db
    with conn:
        cur = conn.cursor() #use cursor method
        #creates a new table named 'tbl_MyFiles' if it doesn't already exist
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_MyFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            text_File TEXT \
            )")
        path = os.getcwd() #get cwd from 'os' module, stored in 'path' 
        fileList = os.listdir(path) #gets the list of files in cwd, stored in 'fileList' 
        entries = [] #create empty list
        for i in fileList: #iterate through tuple 'fileList' with var 'i'
            if i.endswith(".txt"): #look for .txt files
                entries.append((i,)) #append empty 'entries' list with any '.txt' files using (i,) 
        cur.executemany("INSERT INTO tbl_MyFiles(text_File) VALUES (?)", entries) #use wildcare 
        conn.commit()
    conn.close() #close connection to 
    for i in fileList: #for better looking print to consule
        if i.endswith(".txt"):
            print(i)

    
if __name__ == "__main__": #control
    assignment()
    
