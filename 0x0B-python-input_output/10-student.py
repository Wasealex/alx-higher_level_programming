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

    def to_json(self, attrs=None):
        """method that return directory
        """
        obj = self.__dict__.copy()
        if isinstance(attrs, list):
            for item in attrs:
                if not isinstance(item, str):
                    return obj
            my_list = {}
            for idx in range(len(attrs)):
                for satr in obj:
                    if attrs[idx] == satr:
                        my_list[satr] = obj[satr]
            return my_list

        return obj
