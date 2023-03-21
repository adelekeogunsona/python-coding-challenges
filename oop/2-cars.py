#!/usr/bin/pyton3

class Car:
    """
    A class representing a car.
    """

    def __init__(self, make: str, model: str, year: int, color: str, mileage: float):
        """
        Initializes a new instance of the Car class.

        Args:
            make: The make of the car.
            model: The model of the car.
            year: The year the car was manufactured.
            color: The color of the car.
            mileage: The current mileage of the car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage if mileage >= 0 else 0.0

    def drive(self, distance: float) -> None:
        """
        Drives the car for the specified distance.

        Args:
            distance: The distance to drive.

        Returns:
            None.
        """
        if distance >= 0:
            self.mileage += distance

    def get_description(self) -> str:
        """
        Returns a string representation of the car.

        Returns:
            A string representation of the car.
        """
        return f"{self.year} {self.make} {self.model}, {self.color}"

    def paint(self, new_color: str) -> None:
        """
        Paints the car the specified color.

        Args:
            new_color: The new color of the car.

        Returns:
            None.
        """
        self.color = new_color


car1 = Car("Toyota", "Camry", 2018, "White", 10000.5)
car1.drive(100)
assert car1.mileage == 10100.5
assert car1.get_description() == "2018 Toyota Camry, White"

car2 = Car("Honda", "Civic", 2020, "Black", 5000.2)
car2.paint("Red")
assert car2.color == "Red"
assert car2.get_description() == "2020 Honda Civic, Red"

car3 = Car("Ford", "Mustang", 2015, "Blue", 7500.7)
car3.drive(500.3)
car3.paint("Green")
assert car3.mileage == 8001.0
assert car3.color == "Green"
assert car3.get_description() == "2015 Ford Mustang, Green"
