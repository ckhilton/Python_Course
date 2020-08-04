#   PYTHON COURSE
#   ASSIGNMENT: STEP 183
#   AUTHOR: KIRK HILTON

#PARENT CLASS
class staff():
    empFName = "Jerome"
    empLName = "Powell"
    empEmail = "jpowell@fedreserve.org"
    empID = "10129"

    def signIn(self):
        signIn_FName = input("what is your first name? ").lower()
        signIn_LName = input("What is your last name? ").lower()
        signIn_Email = input("What is your Federal email address? ").lower()
        signIn_ID = input("What is your Federal ID number? ").lower()
        if (signIn_FName == self.empFName.lower() and signIn_LName == self.empLName.lower() and signIn_Email == self.empEmail.lower() and signIn_ID == self.empID.lower()):
            print("Welcome, {} {}! An email was sent to '{}'. Please sign in to your email and retrieve the verification link.\n".format(self.empFName,self.empLName,self.empEmail))
        else:
            print("Sorry, your credentials did not match. Please try again.\n")
            #self.signIn()
            
                

                
#CHILD CLASS 1
class secure(staff):
    clearance = "Yes"
    empID = "10129"
    clearance_PIN = "12345"
    
    def signIn(self):
        again = True
        while again:
            signIn_secure = input("Welcome! Do you have a security clearance? (Yes or No): ").lower()
            if (signIn_secure != self.clearance):
                again = False
                print("Thank you!")
            elif (secure == self.clearance and signIn_ID == self.empID and signIn_FName == self.empFName and signIn_LName == self.empLName and signIn_clearance == self.clearance_PIN):
                print("Welcome, {} {}, after you sign into your email {} and verify your identity, you will have access to the Federal Reserve printing press.".format(self.empFName,self.empLName,self.empEmail))
            else:
                print("That's ok, {} {} , you have acces anyways. Happy printing!".format(self.empFName,self.empLName)) 




if __name__ == "__main__": #control code
    employee = staff()
    employee.signIn()

    chairman = secure()
    chairman.signIn()
