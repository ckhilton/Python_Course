#   PYTHON COURSE
#   ASSIGNMENT: STEP 202 (ABSTRACTION)
#   AUTHOR: KIRK HILTON

from abc import ABC, abstractmethod

#PARENT CLASS
class donor(ABC):
    
    def receipt(self, total):
        print("Thank you for your donation of:",total)

    @abstractmethod #USE AN ABSTRACT METHOD BELOW
    def message(self, total):
        pass #NOT DEFINING WHAT DATA THE ARGUMENTS ARE

#CHILD CLASS 1
class cash(donor):
    def message(self, total):
        print("Your cash donation of {} was deposited safely by a representative of the Charity Works Foundation.".format(total))

#CHILD CLASS 2
class online(donor):
    def message(self, total):
        print("Your online donation of {} was accepted by the Charity Works Foundation online.".format(total)) 
        

if __name__ == "__main__": #CONTROL
    
    donation1 = cash()
    donation1.receipt("$25")
    donation1.message("$25")

    donation2 = online()
    donation2.receipt("$25")
    donation2.message("$25")
    
    
