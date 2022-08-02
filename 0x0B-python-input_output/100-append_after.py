#!/usr/bin/python3
"""search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file after
    each line containing a specific string"""
    tmp = ""
    with open(filename) as f:
        for line in f:
            tmp += line
            if search_string in line:
                tmp += new_string
    with open(filename, "w") as w:
        w.write(tmp)
