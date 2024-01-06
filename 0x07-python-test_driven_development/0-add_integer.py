#!/usr/bin/python3
"""this module is "0-add_integer"

    it has one function , add_integer()
    which returns sum of two parameters
"""


def add_integer(a, b=98):
    """add_integer is a function that takes two integers
       args:
            a(int or float) = the first parameter
            b(int or float) = the second parameter
       returns:
               sum = a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum
