class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3*self.radius*self.radius
    


circle1 = Circle(5)

print(circle1.calculateArea())