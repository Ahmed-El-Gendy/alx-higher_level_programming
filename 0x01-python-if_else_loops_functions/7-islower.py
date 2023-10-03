#!/usr/bin/python3
def islower(c):
    if not c:
        raise ValueError("Input string cannot be empty")
    if c >= 'a' and c <= 'z':
        return True
    else:
        return False
