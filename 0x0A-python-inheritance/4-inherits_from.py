#!/usr/bin/python3
"""contains one function, inherits_from
"""


def inherits_from(obj, a_class):
    """comparesed two arguments obj and a_class and returns bool
       True if obj is a subclass, otherwise fasle
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
