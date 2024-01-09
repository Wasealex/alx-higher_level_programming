#!/usr/bin/python3
"""module has one function class_to_json
"""


def class_to_json(obj):
    """return dictionary of description of obj
    """
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
