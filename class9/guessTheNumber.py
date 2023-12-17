import random

randomNum = random.randint(1, 10)

while(True):
    user_num = int(input("Guess the number between 1 to 10: "))
    if(user_num ==  randomNum):
        print("Horrrah! you have won the game")
        break
    else:
        print("try again!")