#!/usr/bin/python3
"""created a class named Square that adds a size as int"""


class Square:
    """initialize the class with a size attribute"""
    def __init__(self, size=0):
        """size must be an intiger and greater than zero"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area is square of one side"""
        area = self.__size ** 2
        return area
