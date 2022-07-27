#!/usr/bin/python3
"""add_integer"""


def add_integer(a, b=98):
    """adds two integers upon validation"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
