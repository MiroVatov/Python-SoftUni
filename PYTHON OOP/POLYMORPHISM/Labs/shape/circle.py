from shape import Shape
from math import pi


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * pi * self.__radius




