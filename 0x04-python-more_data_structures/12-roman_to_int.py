#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last = 0
    s = 0
    for i in reversed(roman_string):
        if dic[i] < last:
            s -= dic[i]
        else:
            s += dic[i]
        last = dic[i]
    return s
