#!/usr/bin/python3
"""a module that contains one class, Base
"""
import json


class Base:
    """class Base containing the base object
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
