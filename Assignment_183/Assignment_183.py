#   PYTHON COURSE
#   ASSIGNMENT: STEP 183
#   AUTHOR: KIRK HILTON

#PARENT CLASS
class user():
    FName = "Jerome"
    LName = "Powell"
    Email = "jpowell@fedreserve.org"
    Pass = "FreeMoney"

    def signIn(self):
        signIn_FName = input("What is your first name? ").lower()
        signIn_LName = input("What is your last name? ").lower()
        signIn_Email = input("What is your Federal email address? ").lower()
        signIn_Pass = input("What is your password? ")
        if (signIn_FName == self.FName.lower() and signIn_LName == self.LName.lower() and signIn_Email == self.Email.lower() and signIn_Pass == self.Pass):
            print("Welcome, {} {}! An email was sent to '{}'. Please sign in to your email to retrieve the verification link.\n".format(self.FName,self.LName,self.Email))
        else:
            print("Sorry, your credentials did not match.\nPlease try again.\n")
            #self.signIn() _an optional loop to give the user multiple tries to sign in.
            
                         
#CHILD CLASS 1
class employee(user):
    salary = "$$$ Infinite $$$"
    position = "chairman"
    clearance_PIN = "12345"

    def signIn(self):
        signIn_FName = input("What is your first name? ").lower()
        signIn_LName = input("What is your last name? ").lower()
        signIn_Email = input("What is your Federal email address? ").lower()
        signIn_PIN = input("What is your Federal ID number? ").lower()
        if (signIn_FName == self.FName.lower() and signIn_LName == self.LName.lower() and signIn_Email == self.Email.lower() and signIn_PIN == self.clearance_PIN.lower()):
            print("Welcome, {} {}!\nYour annual salary is:\n{}!!!\nAs a reminder, you now have access to the Federal Reserve printing press. Enjoy!\n".format(self.position,self.LName,self.salary))
        else:
            print("Sorry, your credentials did not match./nPlease try again.\n")
            #self.signIn() _an optional loop to give the user multiple tries to sign in.

#CHILD CLASS 2
class intern(user):
    FName = "Joe"
    LName = "Schmoe"
    Email = "jschmoe@fedreserve.org"
    ID = "001"
    Pass = "schmoozer"
    Hourly = "$18.00"
    

    def signIn(self):
        signIn_FName = input("What is your first name? ").lower()
        signIn_LName = input("What is your last name? ").lower()
        signIn_Email = input("What is your Federal email address? ").lower()
        signIn_ID = input("What is your internship ID number? ").lower()
        signIn_Intern = input("What is your temporary password? ").lower()
        if (signIn_FName == self.FName.lower() and signIn_LName == self.LName.lower() and signIn_Email == self.Email.lower() and signIn_ID == self.ID.lower() and signIn_Intern == self.Pass):
            print("Welcome, {} {}!\nYour hourly wage is {}.\nAs a reminder, if you don't do what we say, we'll fire you on the spot!".format(self.FName,self.LName,self.Hourly))
        else:
            print("Sorry, your credentials did not match. Please try again.\n")
            #self.signIn() _an optional loop to give the user multiple tries to sign in.


if __name__ == "__main__": #control code
    person = user()
    person.signIn()

    chairman = employee()
    chairman.signIn()

    temp = intern()
    temp.signIn()
