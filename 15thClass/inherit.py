class Animal:
    def breathe(self):
        print("breathing")

    def move(self):
        print("moving")

    def eat(self):
        print("eating")



class Duck(Animal):
    def fly(self):
        print("i can fly")


class specialDuck(Duck):
    def swim(self):
        print("can swim")


duck1 = specialDuck()

print(duck1.breathe())