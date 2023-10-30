#!/usr/bin/python3
"""rectangle"""


class Rectangle:
    """class"""

    def __init__(self, width=0, height=0):
        """class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """class"""
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """class"""
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__height = val
