# global Variable

myAge = 11
# print("global", id(myAge))
def myfunction():

    # myAge = 14
    # print("local", id(myAge))
    # print("age: ", myAge)

    global myAge
    myAge = myAge+1
    print("age: ", myAge)

myfunction()