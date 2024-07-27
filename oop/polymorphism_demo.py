class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectngle(Shape):
    def area(self):
        lenth = int(input("Enter lenth:"))
        width = int(input("Enter width:"))
        area = lenth * width

class Circle(Shape):
    def area(self):
        radius = float(input("Enter radius:"))
        import math
        area = float(math.pi * (radius * radius))
        
