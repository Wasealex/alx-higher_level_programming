#!/usr/bin/python3
"""
    this module is "3-say_my_name"

    it has one function, say_my_name()
    it takes two arguments and prints out on stdout
    prints My name is ...
"""


def say_my_name(first_name, last_name=""):
    """
        function say_my_name takes two arguments and prints them out

    args:
         first_name(str) = first parameter
               it should be a string
         second_name(str) = second parameter
               it is opitional but when given must be a string
    returns:
           None
    output:
           My name is {first_name} {second_name}
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
