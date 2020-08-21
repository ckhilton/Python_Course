

import sqlite3
import os

def create_db():
    conn = sqlite3.connect("Assignment_Step-164.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS My_Files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            FileName TEXT \
            )")
        conn.commit()
    conn.close()

"""
def create_db():
    path = os.getcwd()
    fileList = os.listdir(path)
        def convert(fileList):
        return tuple(*fileList, )
    conn = sqlite3.connect("Assignment_Step-164.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS My_Files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            FileName TEXT \
            )")
        conn.commit()
        #convert(fileList)
        cursor.executemany("INSERT INTO My_Files(FileName) VALUES (?)", fileList)
        conn.commit()
        item = cursor.execute("SELECT * FROM My_Files WHERE FileName LIKE '%txt%'")
        result = item.fetchall()
        for item in result:
            display = "{}\n{}".format(item[0],item[1])  
    conn.close()
    print(display)
"""

def entry():
    path = os.getcwd()
    fileList = os.listdir(path)
    conn = sqlite3.connect("Assignment_Step-164.db")
    with conn:
        cur = conn.cursor()
        entries = []
        for f in fileList:
            entries.append((f,))
            cur.executemany("INSERT INTO My_Files(FileName) VALUES (?)", entries)
        conn.commit()
    conn.close()

def print_to_console():
    conn = sqlite3.connect("Assignment_Step-164.db")
    with conn:
        cur = conn.cursor()
        cur.executemany("SELECT * FROM My_Files WHERE FileName LIKE '%.txt%'")
        result = cur.fetchall()
        for item in result:
            display = "{}".format(item)
    conn.close()
    print(display)


if __name__ == "__main__":
    create_db()
    entry()
    print_to_console()
