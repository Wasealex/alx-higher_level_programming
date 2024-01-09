#!/usr/bin/python3
"""this is a module that contains one function, read_file
"""


def read_file(filename=""):
    """takes one arguments filename and opens it and reads line from
       it
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
