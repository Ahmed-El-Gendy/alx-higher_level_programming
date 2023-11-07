#!/usr/bin/python3
"""to dict"""
import json


def from_json_string(my_str):
    '''from json to dict'''
    return json.loads(my_str)
