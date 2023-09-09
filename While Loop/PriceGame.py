namea = input("Please enter player A's name") 
nameb = input("Please enter player B's name") 
#input玩家姓名

price = int(9000) 
answertimes=0
playingtimes = 3
#設定答案價格及定義回答次數&可挑戰次數

while answertimes < playingtimes:
    answera = int(input(f"Hi, {namea}. Enter the guess price of the items"))
    answerb = int(input(f"Hi,{nameb}. Enter the guess price of the items")) #當回答次數小於可挑戰次數時使玩家輸入猜測金額
    if answera == price:
        print(f"Congratulations! {namea} successfully guess the price:{price}")
        break #若玩家A答對即中斷迴圈並顯示正答訊息
    elif answerb == price:
        print(f"Congratulations! {nameb} successfully guess the price:{price}")
        break #若玩家B答對即中斷迴圈並顯示正答訊息
    elif abs(answera - price) > abs(answerb - price):
        print(f"Good try! But it's wrong, {nameb} is closer to the answer.") 
    elif abs(answera - price) < abs(answerb - price) :
        print(f"Good try! But it's wrong, {namea} is closer to the answer.") #當猜錯價格時比較哪位玩家更接近解答並顯示提示
    answertimes += 1
    print(f"Left {abs(playingtimes - answertimes)} times guessing.") #顯示剩餘挑戰次數
if answertimes == 3 and abs(answera - price) > abs(answerb - price) and answera != 9000 and answerb != 9000:
    print(f"Game over. {nameb} wins! The correct price is {price} and {nameb} guess closet to the price.") 
elif answertimes == 3 and abs(answera - price) < abs(answerb - price) and answera != 9000 and answerb != 9000:
    print(f"Game over. {namea} wins! The correct price is {price} and {namea} guess closet to the price.")
#當挑戰次數達上限顯示最接近答案的玩家獲勝及正確解答
