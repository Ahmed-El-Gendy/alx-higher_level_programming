#!/usr/bin/python3
"""file write"""


def write_file(filename="", text=""):
    """write"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
