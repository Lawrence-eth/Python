namea = input("Please enter player A's name")
nameb = input("Please enter player B's name")

price = int(9000)
answertimes=0
playingtimes = 3

while answertimes < playingtimes:
    answera = int(input(f"Hi, {namea}. Enter the guess price of the items"))
    answerb = int(input(f"Hi,{nameb}. Enter the guess price of the items"))
    if answera == price:
        print(f"Congratulations! {namea} successfully guess the price:{price}")
        break
    elif answerb == price:
        print(f"Congratulations! {nameb} successfully guess the price:{price}")
        break
    elif abs(answera - price) > abs(answerb - price):
        print(f"Good try! But it's wrong, {nameb} is closer to the answer.")
    elif abs(answera - price) < abs(answerb - price) :
        print(f"Good try! But it's wrong, {namea} is closer to the answer.")
    answertimes += 1
    print(f"Left {abs(playingtimes - answertimes)} times guessing.")
if answertimes == 3 and abs(answera - price) > abs(answerb - price) and answera != 9000 and answerb != 9000:
    print(f"Game over. {nameb} wins! The correct price is {price} and {nameb} guess closet to the price.")
elif answertimes == 3 and abs(answera - price) < abs(answerb - price) and answera != 9000 and answerb != 9000:
    print(f"Game over. {namea} wins! The correct price is {price} and {namea} guess closet to the price.")
