## Challenge 1

Create a class called "Shape" that has the following attributes and methods:

Attributes:
```
name (string)
color (string)
```

Methods:
```
get_area() returns the area of the shape
get_perimeter() returns the perimeter of the shape
```
Create two subclasses of "Shape":

"Rectangle" with additional attributes and methods:
```
Attributes:
width (float)
height (float)
```
Methods:
```
get_diagonal() returns the diagonal of the rectangle
```
"Circle" with additional attributes and methods:

Attributes:
```
radius (float)
```

Methods:
```
get_diameter() returns the diameter of the circle
```


Test Case for Rectangle
```
rect = Rectangle("Rectangle", "Blue", 3, 4)
assert rect.get_area() == 12
assert rect.get_perimeter() == 14
assert rect.get_diagonal() == 5
```

Test Case for Circle
```
circle = Circle("Circle", "Red", 5)
assert circle.get_area() == 78.53981633974483
assert circle.get_perimeter() == 31.41592653589793
assert circle.get_diameter() == 10
```

Test Case for Shape
```
shape = Shape("Shape", "Green")
assert shape.get_area() == 0
assert shape.get_perimeter() == 0
```

