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

    @classmethod
    def save_to_file(cls, list_objs):
        """json representation of list of instances who ineherits Base
           to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                list_dictionaries = [kv.to_dictionary() for kv in list_objs]
                f.write(Base.to_json_string(list_dictionaries))
