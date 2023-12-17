num1 = int(input(""))
num2 = int(input(""))
choice = int(input("enter a choice: "))


if choice == 1:
    print(num1+num2)


elif choice == 2:
    print("substract")
elif choice == 3:
    print("divide")
elif choice == 4:
    print("multiply")

else:
    print("out of operation")