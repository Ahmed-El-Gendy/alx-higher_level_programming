#!/usr/bin/python3
"""class inherits from list"""


class MyList(list):
    """print list sorted"""

    def print_sorted(self):
        """print"""
        print(sorted(self))
