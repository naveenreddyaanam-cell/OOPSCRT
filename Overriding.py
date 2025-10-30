# Define a base class.
class Shape:
    def area(self):
        pass
# Define derived classes.
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
# Outside the class definition.
sq = Square(20)
rc = Rectangle(10, 20)
cr = Circle(3)
# Calling the overriding methods of derived classes.
print("Area of square: ", sq.area())
print("Area of rectangle: ", rc.area())
print("Area of circle: ", cr.area())
