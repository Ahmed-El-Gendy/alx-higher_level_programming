#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    v = None
    ma = None
    for i in a_dictionary:
        if not ma or (a_dictionary[i] > ma):
            ma = a_dictionary[i]
            v = i
    return v
