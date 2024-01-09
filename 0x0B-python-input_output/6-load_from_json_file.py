#!/usr/bin/python3
"""a  module containg only one function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """function that creats an obj from json file
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
