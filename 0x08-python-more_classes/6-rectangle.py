#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """class"""

    number = 0

    def __init__(self, width=0, height=0):
        """class"""
        self.width = width
        self.height = height
        type(self).numper += 1

    @property
    def width(self):
        """class"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """class"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """pre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """return list"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        pr = []
        for i in range(self.__height):
            for j in range(self.__width):
                pr.append('#')
            if i != self.height - 1:
                pr.append("\n")
        return ("".join(pr))

    def __repr__(self):
        """size"""
        pr = "Rectangle(" + str(self.__width) + ", " + str(self.height) + ")"
        return (pr)

    def __del__(self):
        """delete"""
        print("Bye rectangle...")
        type(self).numper += 1
