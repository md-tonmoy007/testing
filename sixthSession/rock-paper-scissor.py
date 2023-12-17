
import random

randomNum = random.randint(0,2)
call = ["r", "p", "s    "]

computer = call[randomNum] # "r" or "p" or "s"
user = input("type r/p/s : ")

if (computer == user):
    print(f"computer: {computer} and user: {user}")
    print("draw")

elif(user == "r"):
    if (computer == "p"):
        print(f"computer: {computer} and user: {user}")
        print("you lose")
    else:
        print(f"computer: {computer} and user: {user}")
        print("yout won")

elif(user == "p"):
    if (computer == "s"):
        print(f"computer: {computer} and user: {user}")
        print("you lose")
    else:
        print(f"computer: {computer} and user: {user}")
        print("yout won")

elif(user == "s"):
    if (computer == "r"):
        print(f"computer: {computer} and user: {user}")
        print("you lose")
    else:
        print(f"computer: {computer} and user: {user}")
        print("yout won")