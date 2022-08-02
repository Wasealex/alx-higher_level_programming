#!/usr/bin/python3
"""module student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of student"""
        if attrs is None:
            return self.__dict__
        if (isinstance(attrs, list) and
                all(type(ele) == str for ele in attrs)):
            return {v: getattr(self, v) for v in attrs if hasattr(self, v)}
