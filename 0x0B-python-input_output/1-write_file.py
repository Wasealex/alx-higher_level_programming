#!/usr/bin/python3
"""a module that contains write_file
"""


def write_file(filename="", text=""):
    """function opens file and overwrites text
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
