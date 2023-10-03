#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        return number % 10
    return abs(number % 10) * -1
print_last_digit(98)
