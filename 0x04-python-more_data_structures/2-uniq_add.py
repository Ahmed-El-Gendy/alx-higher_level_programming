#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if len(my_list) == 0:
        return 0
    s = {my_list[0]}
    s.update(my_list)
    for i in s:
        sum += i
    return sum
