#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.keys())
    for i in dic:
        print("{}: {}".format(i, dic[i]))
