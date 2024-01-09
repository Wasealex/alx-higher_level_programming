#!/usr/bin/python3
"""a module that contains one function from_json_string
"""
import json


def from_json_string(my_str):
    """a function that loads json from an obj
    """
    return json.loads(my_str)
