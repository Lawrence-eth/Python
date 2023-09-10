import random
import string
number = string.digits
letters = string.ascii_letters
alphabet = list(number + letters)
random.shuffle(alphabet)
pwlen = int(input(f"Please enter the length of the password you want to generate"))
password = alphabet[:pwlen]
print(f"{password}")

