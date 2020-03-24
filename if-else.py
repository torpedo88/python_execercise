class FizzBuzz :

    def __init__(self,value):
        self.value = value
    value = int(input(f"Enter the value :"))

        
    if value % 5 == 0 and value % 3 == 0:
        print(f"FizzBizz")
    elif value % 5 == 0:
        print(f"Fizz")
    elif value % 3 == 0:
        print(f"Bizz")
    else:
        pass

