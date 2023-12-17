a = int(input("A: "))
b = int(input("B: "))


choice = int(input("choice operation:"))

if(choice == 1):
    print(a+b)

elif(choice == 2):
    print(a-b)

elif(choice == 3):
    print(a*b)

elif(choice == 4):
    print(a/b)

else:
    print("wrong operation")