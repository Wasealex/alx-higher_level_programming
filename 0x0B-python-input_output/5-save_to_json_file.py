#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a textfile using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
