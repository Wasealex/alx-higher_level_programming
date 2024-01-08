#!/usr/bin/python3
"""a module contains one function, is_same_class
"""


def is_same_class(obj, a_class):
    """function takes to arguments and compares them for having
       exact instance and returns True or False
    Args:
         obj = the first parameter
         a_class = the second parameter
    Returns:
           bool: True if obj and a_class have exact instance
                 False if not
    """
    return (type(obj) == a_class)
