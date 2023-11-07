#!/usr/bin/python3
"""my int class"""


class MyInt(int):
    """invert int"""

    def __feq__(self, value):
        """== to !="""
        return self.read != value

    def __ne__(self.value):
        """!= to =="""
        return self.real == value
