#!/usr/bin/python3
'''save to json'''
import json


def save_to_json_file(my_obj, filename):
    '''save'''
    with open(my_obj, 'w') as f:
        json.dump(my_obj, f)
