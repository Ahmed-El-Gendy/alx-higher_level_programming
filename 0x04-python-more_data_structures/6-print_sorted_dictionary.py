#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = dict(sorted(a_dictionary.items()))
    for i in a_dictionary:
        print("{}: {}".format(i, a_dictionary[i]))
