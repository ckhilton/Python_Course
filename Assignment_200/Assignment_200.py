#   PYTHON COURSE
#   ASSIGNMENT: STEP 200 (ENCAPSULATION)
#   AUTHOR: KIRK HILTON

#PARENT CLASS 
class car():
    
    def __init__(self):
        self.model = input("What model of car do you own?: ")
        self._protectedVar = self.model
        self.year = input("What year is your car?: ")
        self.__privateVar = self.year

    def getBoth(self):
        print("\nThis is the protected variable: '{}'".format(self.model))
        print("This is the private variable: '{}'".format(self.year))

    def setBoth(self, protected, private):
        self._protectedVar = protected
        print("\nThe reset protected variable is now: '{}'".format(protected))
        self.__privateVar = private
        print("The reset private variable is now: '{}'".format(private))


if __name__ == "__main__": #CONTROL
    new = car() #Create new car object called "new"
    new.getBoth() #Calls on getBoth
    new.setBoth("Toyota","2011") #Uses setBoth() to reset the variables

   
   
        
