#!/usr/bin/python3
from math import pi, sqrt

class Shape:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
    

    # returns the area of the shape
    def get_area(self):
        return 0
    

    # returns the perimeter of the shape
    def get_perimeter(self):
        return 0


class Rectangle(Shape):

    def __init__(self, name: str, color: str, width: float, height: float):
        super().__init__(name, color)
        self.width = width
        self.height = height


    # returns area of the rectangle
    def get_area(self):
        return self.width * self.height


    # returns the perimeter of the rectangle
    def get_perimeter(self):
        return 2 * (self.width + self.height)


    # returns the diagonal of the rectangle
    def get_diagonal(self):
        return sqrt((self.width**2) +  (self.height**2))


class Circle(Shape):

    def __init__(self, name: str, color: str, radius: float):
        super().__init__(name, color)
        self.radius = radius
    

    # returns area of the circle
    def get_area(self):
        return pi * (self.radius**2)


    # returns the perimeter of the rectangle
    def get_perimeter(self):
        return 2 * (pi * self.radius)


    # returns the diameter of the circle
    def get_diameter(self):
        return 2 * self.radius


# Rectangle
rect = Rectangle("Rectangle", "Blue", 3, 4)
assert rect.get_area() == 12
assert rect.get_perimeter() == 14
assert rect.get_diagonal() == 5

# Circle
circle = Circle("Circle", "Red", 5)
assert circle.get_area() == 78.53981633974483
assert circle.get_perimeter() == 31.41592653589793
assert circle.get_diameter() == 10

# Shape
shape = Shape("Shape", "Green")
assert shape.get_area() == 0
assert shape.get_perimeter() == 0
