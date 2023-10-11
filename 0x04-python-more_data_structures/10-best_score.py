#!/usr/bin/python3
def best_score(a_dictionary):
    ma = -1
    v = None
    for i in a_dictionary:
        if a_dictionary[i] > ma:
            ma = a_dictionary[i]
            v = i
    return v
