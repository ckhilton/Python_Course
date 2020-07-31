#   PYTHON COURSE
#   ASSIGNMENT: STEP 175
#   AUTHOR: KIRK HILTON

class Person:
    def __init__(self, fname, lname): #initialize object 'Person' with parameters 
        self.firstname = fname #attach 'fname' parameter to attribute
        self.lastname = lname #attach 'lname' parameter to attribute
    def printname(self): 
        print("Hello there", self.firstname, self.lastname)

class Graduate(Person):
  def __init__(self, fname, lname, school, year): #initialize
    super().__init__(fname, lname) #use super() to inherit parent class methods and attributese
    self.collegeName = school
    self.graduationYear = year
  def congrats(self): #create print function
    print("Congratulations", self.firstname, self.lastname, "on graduating from", self.collegeName, "in the year", self.graduationYear)

class Teacher(Person):
  def __init__(self, fname, lname, subject, years): #initialize
    super().__init__(fname, lname) #use super() to inherit parent class methods and attributes
    self.teachingSubject = subject
    self.teachingYears = years
  def thanks(self): #create print function
    print("Thank you", self.firstname, self.lastname, "for teaching", self.teachingSubject, "for the last", self.teachingYears, "years")


if __name__ == "__main__": #control code
    x = Person("Joe", "Schmoe")
    x.printname() #call and print instance of Person class

    y = Graduate("Kirk", "Hilton", "UCDH", 2014)
    y.congrats() #call and print instance of Graduate class

    z = Teacher("Mary", "Poppins", "acting", 30)
    z.thanks() #call and print instance of Teacher class
