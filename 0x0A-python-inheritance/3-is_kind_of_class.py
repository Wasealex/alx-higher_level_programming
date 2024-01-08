#!/usr/bin/python3
"""contains one function, is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """compares the to argumments and returns
       bool if a_class is instance of obj
    """
    return (isinstance(obj, a_class))
