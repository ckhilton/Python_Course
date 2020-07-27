

def doThis():
    a = input("Please tell me your first name: ")
    b = input("Please tell me your last name: ")
    nowThis(a,b)

def nowThis(a,b):
    try:
        c = str(a) +  str(b)
        print("Your printed name is {} {}".format(a,b,c))
    except:
        print("Please try again!")
          
        
    





if __name__ == "__main__":
    doThis()
