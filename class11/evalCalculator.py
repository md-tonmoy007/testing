# print(eval("1+2+3-4")) # takes an string expression as mathematical statement and solves it

def evaluation(expression):
    print(eval(expression))


statement = input("Write a math expression: ")
evaluation(statement)

