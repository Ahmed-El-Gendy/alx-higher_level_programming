#!/usr/bin/python3
def max_integer(my_list=[]):
    ma = -999999
    for i in range (len(my_list)):
        if my_list[i] > ma:
            ma = my_list[i]
    return ma
