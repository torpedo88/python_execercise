#!/usr/bin/env python3.7

upper_number = int(input(f"Enter the upper number :"))

for number in range(1,upper_number + 1):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Fizz")
    
    elif number % 3 == 0:
        print("Buzz")
    
    else:
        print(number)



