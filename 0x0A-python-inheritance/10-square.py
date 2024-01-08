#!/usr/bin/python3
"""module containg subclass Square of Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a represantaion of square
    """
    def __init__(self, size):
        """instantiation of square with attributes of Rectangle class
           and its characterstics including area and validator
        """
        super().__init__(size, size)
