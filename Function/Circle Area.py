def circle_area(r):
    pi= 3.14159265359
    return pi * r * r
#定義圓面積公式
sidelen = int(input(f"Please enter the side length to calculate the area of circle.")) #使用者輸入圓半徑
roundnum = int(input(f"Round to how many decimal places?")) #使用者決定要四捨五入至小數點後位數
print(f"The area of circle is about {round(circle_area(r = sidelen),roundnum)}")
