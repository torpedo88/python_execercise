
'''def spilt_name(name):
    names = name.split()
    first_name = names[0]
    last_name  = names[-1]
    return {
        "First Name": first_name,
        "Last Name": last_name
    }
    

user_input = str(input(f"Enter your full name : "))
print(spilt_name(user_input)) '''

def is_palindrome(item):
    return item == item[::-1]

user_input = str(input(f"Enter the word : "))

if is_palindrome(user_input) == True:
    print(f"Yes!!!! the word is palidrone")

else:
    print("No there is no Palidrone words")





 