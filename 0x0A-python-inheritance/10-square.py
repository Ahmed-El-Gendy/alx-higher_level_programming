#!/usr/bin/python3
"""ractangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__init__(size, size)
        self.__size = size
