

import sqlite3



def create_db():
    conn = sqlite3.connect("test.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fName TEXT, \
            col_lName TEXT, \
            col_email TEXT \
            )")
        conn.commit()
    conn.close()

def entry():
    conn = sqlite3.connect("test.db")
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_persons(col_fName, col_lName, col_email) VALUES (?,?,?)", \
                    ("Sarah", "Jones", "sjones@gmail.com"))
        cur.execute("INSERT INTO tbl_persons(col_fName, col_lName, col_email) VALUES (?,?,?)", \
                    ("Sally", "May", "smay@gmail.com"))
        cur.execute("INSERT INTO tbl_persons(col_fName, col_lName, col_email) VALUES (?,?,?)", \
                    ("Kevin", "Bacon", "kbacon@rocketmail.com"))
       
        conn.commit()
    conn.close()


def print_to_console():
    conn = sqlite3.connect("test.db")
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_fName, col_lName, col_email FROM tbl_persons WHERE col_fName = 'Sarah'")
        varPerson = cur.fetchall()
        for item in varPerson:
            msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
        print(msg)
    

if __name__ == "__main__":
    create_db()
    entry()
    print_to_console()
    
