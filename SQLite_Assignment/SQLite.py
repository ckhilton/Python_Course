

import sqlite3

##firstName = input("Enter your first name: ")
##lastName = input("Enter your last name: ")
##age = int(input("Enter your age: "))
##personData = (firstName, lastName, age)

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

def new():
    with sqlite3.connect('test_database.db') as connection:
        c = connection.cursor()
        c.execute("DROP TABLE IF EXISTS People")
        c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")


def userData():
    with sqlite3.connect('test_database.db') as connection:
        c = connection.cursor()
        #c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
        c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

##def fetchall():
##    with sqlite3.connect('test_database.db') as connection:
##        c = connection.cursor()
##        c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
##        for row in c.fetchall():
##            print(row)

def fetchone():
    with sqlite3.connect('test_database.db') as connection:
        c = connection.cursor()
        c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
        while True:
            row = c.fetchone()
            if row is None:
                break
            print(row)
        
          
def update():
    with sqlite3.connect('test_database.db') as connection:
        c = connection.cursor()
        c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
                  (45, 'Luigi', 'Vercotti'))
     

if __name__ == "__main__":
    new()
    userData()
    #fetchall()
    fetchone()
    update()
    
    
    
