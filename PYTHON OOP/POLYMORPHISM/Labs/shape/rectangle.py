from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return (self.__width * 2) + (self.__height * 2)