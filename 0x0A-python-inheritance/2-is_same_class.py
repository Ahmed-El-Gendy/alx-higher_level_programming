#!/usr/bin/python3
"""returns True if the object is exactly an instance of same class"""


def is_same_class(obj, a_class):
    """is instance"""
    if type(obj) == a_class:
        return (True)
    return (False)
