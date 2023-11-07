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
