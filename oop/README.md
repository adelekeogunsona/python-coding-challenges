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

## Challenge 2
Create a class called "Car" that has the following attributes:
```
make (string)
model (string)
year (integer)
color (string)
mileage (float)
```

The class should have the following methods:
```
init: Initializes the attributes of the car object

drive: Accepts a distance (float) as input and adds it to the mileage of the car

get_description: Returns a string that describes the car (e.g. "2018 Toyota Camry, White")

paint: Accepts a new color (string) as input and changes the color of the car
```

Test Cases:
```
car1 = Car("Toyota", "Camry", 2018, "White", 10000.5)
car1.drive(100)
assert car1.mileage == 10100.5
assert car1.get_description() == "2018 Toyota Camry, White"
```
```
car2 = Car("Honda", "Civic", 2020, "Black", 5000.2)
car2.paint("Red")
assert car2.color == "Red"
assert car2.get_description() == "2020 Honda Civic, Red"
```
```
car3 = Car("Ford", "Mustang", 2015, "Blue", 7500.7)
car3.drive(500.3)
car3.paint("Green")
assert car3.mileage == 8001.0
assert car3.color == "Green"
assert car3.get_description() == "2015 Ford Mustang, Green"
```

## Challenge 3
Create a class called "BankAccount" that has the following attributes:
```
account_number (integer)
owner (string)
balance (float)
```

The class should have the following methods:
```
init: Initializes the attributes of the bank account object

deposit: Accepts a deposit amount (float) as input and adds it to the balance of the account

withdraw: Accepts a withdrawal amount (float) as input and subtracts it from the balance of the account if the balance is sufficient. If the balance is not sufficient, the withdrawal should not be allowed and an error message should be printed.

get_balance: Returns the current balance of the account

transfer: Accepts a transfer amount (float) and a destination account (BankAccount object) as input, and transfers the amount from the current account to the destination account if the balance is sufficient. If the balance is not sufficient, the transfer should not be allowed and an error message should be printed.
```

Test Cases:
```
account1 = BankAccount(123456, "John Smith", 1000.0)
account2 = BankAccount(987654, "Jane Doe", 500.0)

account1.deposit(200.0)
assert account1.get_balance() == 1200.0

account1.withdraw(300.0)
assert account1.get_balance() == 900.0

account1.transfer(500.0, account2)
assert account1.get_balance() == 400.0
assert account2.get_balance() == 1000.0

account1.withdraw(1000.0) # This should print an error message and not change the balance
assert account1.get_balance() == 400.0
```