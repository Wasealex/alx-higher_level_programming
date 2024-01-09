#!/usr/bin/python3
"""a module contains one function, save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes objets to a file
       json representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
