#!/usr/bin/python3
"""ractangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return super().__width * super().__height

    def __str__(self):
        """str"""
        string = "[" + str(super().__class__.__name__)
        string += "] " + str(super().__width) + "/" + str(super().__height)
        return string
