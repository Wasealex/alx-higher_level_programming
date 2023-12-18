#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        functions = fct(*args)
    except Exception as message:
        functions = None
        print("{}".format(message), file=stderr)
    finally:
        return functions
