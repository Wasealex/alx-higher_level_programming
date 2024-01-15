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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string represenation of argument
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionary)
            return instance

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

    @classmethod
    def load_from_file(cls):
        """loads from file json represantion from .json files
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in list_dictionaries]
        except IOError:
            return []
