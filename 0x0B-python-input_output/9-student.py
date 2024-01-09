#!/usr/bin/python3
"""contain a class Student
"""


class Student:
    """create student instance
    """
    def __init__(self, first_name, last_name, age):
        """instatation with basic informations
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that return directory
        """
        return self.__dict__.copy()
