#!/usr/bin/python3
"""a module with a function append_write
"""


def append_write(filename="", text=""):
    """function append_write takes two arguments and
       returns a file appended text
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
