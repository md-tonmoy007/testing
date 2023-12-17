age = int(input("age: "))
nationality = input("enter your nationality: ")
voterID = int(input("VoterID: "))


# and operator 

if(age>=18 and nationality == "bangladeshi" and voterID==1):
    print("u r eligible")

else:
    print("u r not")