#   ASSIGNMENT: STEP 175
#   AUTHOR: KIRK HILTON

class club_member:
    fName = ""
    lName = ""
    phone = ""
    email = ""
    password = ""
    def __init__(self,fName,lName,phone,email,password):
	    self.fName = fName
	    self.lName = lName
	    self.phone = phone
	    self.email = email
	    self.password = password
		

def login(self):
    entry_fName = input("Enter your first name: ")
    entry_phone = input("Enter your phone number: ")
    if (entry_fName == self.fName and entry_phone == self.phone):
        print("Hello {}!".format(self.fName))
    else:
        print("Unauthorized")


new_member = club_member("Kirk","Hilton","801-310-4722","khilton@gmail.com","HeyBaby!")

'''
class child(member):
    waiver = True
    parent = "Full Name"

class adult(member):
    ID = True
    waiver = True
'''




if __name__ ==  "__main__":
    login()
  
    
    
    
