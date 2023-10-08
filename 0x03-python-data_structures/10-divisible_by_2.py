#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lis = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            lis.append(True)
        else:
            lis.append(False)
    return lis
