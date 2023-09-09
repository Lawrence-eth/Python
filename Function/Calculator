def addition (x,y):
    return x + y
#定義加法函數並回傳結果
def subtraction (x,y):
    return x - y
#定義減法函數並回傳結果
def multiplication (x,y):
    return x * y
#定義乘法函數並回傳結果
def division (x,y):
    quotient =  x//y #取商數
    remainder = x % y #取餘數
    return quotient, remainder #回傳商數＆餘數

while True : #重複執行迴圈
    calculate_type = input(f"Please enter the type of calculation. (1) addition (2) subtraction (3) multiplication (4) division") #選擇運算類型
    if calculate_type in ('1', '2', '3', '4'): #檢查運算類型是否為加減乘除四種
        num1 = int(input(f"Please enter the first number to calculate")) #使用者輸入第一個運算數字並指派為num1
        num2 = int(input(f"Please enter the second number to calculate")) #使用者輸入第二個運算數字並指派為num2
        if calculate_type == '1': #若使用者input第一種運算類型則print加法運算結果
            print(f"{num1} and {num2} equals {addition(num1, num2)}")
        elif calculate_type == '2': #若使用者input第二種運算類型則print減法運算結果
            print(f"{num1} from {num2} leaves {subtraction(num1,num2)}")
        elif calculate_type == '3': #若使用者input第三種運算類型則print乘法運算結果
            print(f"{num1} multiplied by {num2} equals {multiplication(num1,num2)}")
        elif calculate_type == '4': #若使用者input第四種運算類型則print除法運算結果
            if num2 == 0: #若除數為0則顯示錯誤訊息
                print(f"Can't divided by 0")
            elif num1 % num2 == 0 : #若運算數字可整除顯示商數（tuple0）
                print(f"{num2} into {num1} goes {division(num1,num2)[0]}")
            else: #若運算數字無法整除顯示商數＆餘數（tuple0、tuple1）
                print(f"{num2} into {num1} goes {division(num1,num2)[0]}, and {division(num1,num2)[1]} remainder")
    else: #若使用者在選擇運算類型時輸入無效指令則顯示結束訊息並終止迴圈
        print(f"End.")
        break
