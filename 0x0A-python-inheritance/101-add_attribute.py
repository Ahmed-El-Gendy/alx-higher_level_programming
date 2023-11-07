#!/usr/bin/python3
"""add attribute"""



def add_attribute(obj, attribute , val):
    """add attribute to obj"""
    if not isinstance(obj, type):
    raise TypeError("can't add new attribute")
    obj.__dict__[attribute] = val
