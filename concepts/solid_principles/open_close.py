# Open Close Principle: States that the entities should be open for extensions but closed for modification

# Incorrect: In the future, if triangle was to be added to shape, the code would have to be modified

import math
from abc import abstractmethod


class Shapes:
    def __init__(self):
        pass

    def area(self, shape_type: str, length: int, breadth: int, radius: int):
        if shape_type == "Rect":
            return length * breadth
        elif shape_type == "Circ":
            return math.pi * radius * radius


# Correct: As many new shapes can now be added without modifying existing code.

class Shape:
    def __init__(self):
        pass

    @abstractmethod
    def area(self) -> int:
        raise Exception("Base class does not have the area method implemented.")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self) -> int:
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> int:
        return math.pi * self.radius ** 2
