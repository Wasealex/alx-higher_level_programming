#!/usr/bin/python3
"""contains one function, lookup()
"""


def lookup(obj):
    """function lookup() takes one argument and returns list of available
       attribute and methods of an object
    Args:
         obj = the only parameter
    Returns:
            list of dir
    """
    return dir(obj)
