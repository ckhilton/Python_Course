



def myFunction(x):
    if x == "":
        print("type your name")
    else:
        print("Hello Kirk")
        
myFunction("Kirk")


family = ["Steph", "Kirk", "Brighton", "Lily", "Maisy"]

family.sort()
print(family)

for i in family:
    print("{} is a member of the Hilton family.".format(i))



y = lambda: 3+3

print(y())
