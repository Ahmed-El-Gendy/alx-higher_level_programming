#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            j = chr(ord(i) - ord('a') + ord('A'))
            print(j, end='')
        else:
            print(i, end='')
