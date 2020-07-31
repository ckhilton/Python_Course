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
  def __init__(self, fname, lname, school, year):
    super().__init__(fname, lname)
    self.collegeName = school
    self.graduationYear = year
  def congrats(self):
    print("Congratulations", self.firstname, self.lastname, "on graduating from", self.collegeName, "in the year", self.graduationYear)

class Teacher(Person):
  def __init__(self, fname, lname, subject, years):
    super().__init__(fname, lname)
    self.teachingSubject = subject
    self.teachingYears = years
  def thanks(self):
    print("Thank you", self.firstname, self.lastname, "for teaching", self.teachingSubject, "for the last", self.teachingYears, "years")

x = Person("Joe", "Schmoe")
x.printname()

y = Graduate("Kirk", "Hilton", "UCDH", 2014)
y.congrats()

z = Teacher("Mary", "Poppins", "acting", 30)
z.thanks()
