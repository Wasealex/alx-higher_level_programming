#!/usr/bin/pyhton3
"""
a module who has function to_json_string
that takes an object
"""
import json


def to_json_string(my_obj):
    """
    a function that representation of json of an obj
    returns json
    """
    return json.dumps(my_obj)
