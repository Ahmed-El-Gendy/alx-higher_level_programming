#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the class functions"""

    def __init__(self, width, height):
        """def"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""
        return self.__height * self.__width

    def __str__(self):
        """print"""
        string = "[" + str(self.__class__.__name__)
        string += "]" + str(self.__width)
        string += "/" + str(self.__height)
        return string
