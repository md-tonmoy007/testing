
import turtle

# fo = open("hi.txt", "r")

# print(fo.read())
# fo.close()

with open("myFolder/hi.txt", "r") as fo:
    print(fo.read())


for i in range(0, 6):
    turtle.forward(50)
    turtle.left(60)



    # 90 - 4 ta
    # 60 - 6 ta
    # 45 - 8 ta

turtle.mainloop()