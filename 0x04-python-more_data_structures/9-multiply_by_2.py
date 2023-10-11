#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {key: value for key, value in a_dictionary.items()}
    for i in dic:
        dic[i] *= 2
    return dic
