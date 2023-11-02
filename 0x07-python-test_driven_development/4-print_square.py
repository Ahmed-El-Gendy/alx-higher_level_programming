#!/usr/bin/python3
def print_square(size):

    if not isinstance(size, (int, float)) or size != int(size):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)

    if size == 0:
        return
    for _ in range(size):
        print("#" * size)
