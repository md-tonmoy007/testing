def adder(a, b):
    print(a+b)

def substract(a, b):
    print(a - b)


num1 = int(input("a: "))
num2 = int(input("b: "))

choice = input(" choose between ( + / -) ")

if(choice == "+"):
    adder(num1, num2)
elif(choice == "-"):
    substract(num1,num2)
else:
    print("wrong operation")