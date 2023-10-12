#!/usr/bin/python3
def roman_to_int(roman_string):
    s = 0
    if roman_string == None:
        return 0
    dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
    for i in roman_string:
        if i in dic:
            s += dic[i]
        else:
            return 0
    return s
