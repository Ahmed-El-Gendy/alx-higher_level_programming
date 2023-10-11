#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mat = my_list[:]
    sq = list(map(lambda x: x if x != search else replace, mat))
    return sq
