#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_dic = {}
    for i in set_1:
        if i in my_dic:
            my_dic[i] = my_dic[i] + 1
        else:
            my_dic[i] = 1
    for i in set_2:
        if i in my_dic:
            my_dic[i] = my_dic[i] + 1
        else:
            my_dic[i] = 1
    li = []
    for i in my_dic:
        if my_dic[i] > 1:
            li.append(i)
    return li
