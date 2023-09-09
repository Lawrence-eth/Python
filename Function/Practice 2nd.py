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
    calculation_type = input(f"Please enter the type of calculation (1)/add: Addition (2)/sub: Subtraction (3)/mul: Multiplication (4)/div: Division")
    if calculation_type in ("1","2","3","4","add","sub","mul","div"): #新增了透過輸入 add/sub/mul/div 來指定運算類型的選項
        num1 = int(input(f"Please enter the first number to calculate."))
        num2 = int(input(f"Please enter the second number to calculate."))
        if calculation_type == "1" or calculation_type == "add":
            print(f"{num1} and {num2} equals {addition(num1, num2)}.")
        elif calculation_type == "2" or calculation_type == "sub":
            print(f"{num1} from {num2} leaves {subtraction(num1, num2)}.")
        elif calculation_type == "3" or calculation_type == "mul":
            print(f"{num1} multiplied by {num2} equals {multiplication(num1, num2)}")
        elif calculation_type == "4" or calculation_type == "div":
            if num2 == 0:
                print(f"Can't divide by 0 !!!")
            elif num1 % num2 == 0:
                print(f"{num2} into {num1} goes {division(num1, num2)[0]}")
            else:
                print(f"{num2} into {num1} goes {division(num1, num2)[0]}, and {division(num1, num2[1])} remainder.")
    else:print(f"Terminated")