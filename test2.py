from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3,14 * (self.radius ** 2)

# Testy
from unittest.mock import patch

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 2) == 28.27

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass