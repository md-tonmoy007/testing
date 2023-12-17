class Person:
    # eyecolor, hairColor, height, weight, age
    def __init__(self, eyecolor, hairColor, height, weight, age):

        self.eyecolor = eyecolor
        self.hairColor = hairColor
        self.height = height
        self.weight = weight
        self.age = age
        # pass

    def nothing(self):
        print("nothing")

ed_sheeran = Person("blue", "ginger", 170, 80, 30)
jifat = Person("black", "black",178, 80, 21 )


print(ed_sheeran.hairColor)
print(jifat.nothing())