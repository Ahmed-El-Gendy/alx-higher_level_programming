#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """the class functions"""

    def __init__(self, width, height):
        """def"""
        self.integer_validator("wid", width)
        self.__width = width
        self.integer_validator("heigh", height)
        self.__height = height
