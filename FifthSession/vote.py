# 2 condition 
# condition - 1: age > 18
# codintion - 2: nationality = Bangladeshi

age = int(input("enter your age: "))



if(age >= 18):
    nationality = input("enter your nationality: ")
    if(nationality == "bangladeshi"):
        print("you are eligible for voting")
    
else:
    print("you r not eligible for voting")