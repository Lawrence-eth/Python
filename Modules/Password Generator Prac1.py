import random
import string
#import 隨機及字串模組
number = string.digits #匯入string模組中的digits為數字
letters = string.ascii_letters #匯入string模組中的字母為英文字母
alphabet = list(number + letters) #字母表為所有英文＆數字 #轉為list否則後面無法shuffle
pwlen = int(input(f"What is the length of the password you want to generate? (Type only numbers)")) #使用者輸入密碼長度
random.shuffle(alphabet) #打亂字母表 #print(f"{alphabet}")錯誤因str無法shuffle
password = ''.join(alphabet[:pwlen])
print(f"{password}")



