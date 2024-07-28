class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.lenth = int(input("Enter lenth:"))
        self.width = int(input("Enter width:"))
        area = self.lenth * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        self.radius = float(input("Enter radius:"))
        import math
        area = float(math.pi * (self.radius)**2)
        
        
