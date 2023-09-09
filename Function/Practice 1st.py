def addition (x,y):
    return x + y
def subtraction (x,y):
    return x - y
def multiplication (x,y):
    return x * y
def division (x,y):
    quotient = x//y
    remainder = x % y
    return quotient, remainder
#definition completed

while True:
    calculation_type = input(f"Please enter the type of calculation (1) Addition (2) Subtraction (3) multiplication (4) Division. (Press any other key to end the program)")
    if calculation_type in ("1","2","3","4"):
        num1 = int(input(f"Please enter the first number to calculate")) #預設情況下input的data type為str，進行運算需轉換為int
        num2 = int(input(f"Please enter the second number to calculate"))
        if calculation_type == "1":
            print(f"{num1} and {num2} equals {addition(num1, num2)}.")
        elif calculation_type == "2":
            print(f"{num1} from {num2} leaves {subtraction(num1, num2)}.")
        elif calculation_type == "3":
            print(f"{num1} multiplied by  {num2} equals {multiplication(num1, num2)}.")
        elif calculation_type == "4":
            if num2 == 0:
                print(f"Can't divide by 0")
            elif num1 % num2 == 0:
                print(f"{num2} into {num1} goes {division(num1, num2)[0]}.")
            else:
                print(f"{num2} into {num1} goes {division(num1, num2)[0]}, and {division(num1, num2)[1]} remainder.")
    else:
        print(f"Terminated.")
