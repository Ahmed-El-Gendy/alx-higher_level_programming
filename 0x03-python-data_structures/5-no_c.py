#!/usr/bin/python3
def no_c(my_string):
    st = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            st += c
    return st
