# w3resource exercise 


import random

randomNum = random.randint(1, 10)

for i in range(0, 4):
    user_num = int(input("Guess the number between 1 to 10: "))
    if(user_num ==  randomNum):
        print("Horrrah! you have won the game")
        break

    
    elif (i >= 3):
        print("you lose the game")
        print(f"the number was {randomNum}")
    elif (user_num > randomNum):
        print("high")
    elif (user_num < randomNum):
        print("low")
    

    else:
        print("try again!")