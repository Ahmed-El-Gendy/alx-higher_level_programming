#!/usr/bin/python3
"""my int class"""


class MyInt(int):
    """invert int"""

    def __eq__(self, value):
        """== to !="""
        return self.real != value

    def __ne__(self, value):
        """!= to =="""
        return self.real == value
