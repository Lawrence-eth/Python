import random
import string
number = string.digits
letters = string.ascii_letters
alphabet = list(number + letters) #預設的data type 為str，應先轉為list才能用於後面的shuffle
pwlen = int(input(f"Please enter the length of the password you want to generate."))
random.shuffle(alphabet)
password = ''.join(alphabet[:pwlen]) #join語法將清單轉成易讀字串
print(f"{password}")
#print(alphabet)
#result : shuffled alphabet
