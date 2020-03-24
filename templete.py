'''
class Users:
    def my_users(self, fname, lname, fullname):
        self.fname = fname
        self.lname = lname
        self.fullname = fullname
    fname = input(str(f"Please Enter your First Name :"))
    lname = input(str(f"Please Enter your Last Name :"))
    fullname = fname +" "+ lname
    
    
    def my_tech(self, tech):
        self.tech = tech
    tech = input(str(f"What is the favriout tech you have been working :"))

  
    templete = "Hello, my name is {}" + " " + "and i really enojoy {}, Have a nice day !!!"
    print(templete.format (fullname, tech))
    
    '''


message = input(f"Please enter a message :")

print(f"Upper :", message.upper())
print(f"Lower :", message.lower())
print(f"Capitalized :",message.capitalize())
print("Title :", message.title())
         
    

