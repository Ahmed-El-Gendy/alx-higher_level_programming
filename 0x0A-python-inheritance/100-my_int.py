#!/usr/bin/python3
"""my int class"""


class MyInt(int):
    """invert int"""

    def __eq__(self, value):
        """== to !="""
        return not super().__eq__(value)

    def __se__(self, value):
        """!= to =="""
        return not super().__ne__(value)
