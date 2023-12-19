#!/usr/bin/python3
"""created a class named Square that adds a size as int"""


class Square:
    """initialize the class with a size attribute"""
    def __init__(self, size=0):
        """size must be an intiger and greater than zero"""
        self.__size = size

    @property
    def size(self):
        """return size of square as property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """validate value"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area is square of one side"""
        area = self.__size ** 2
        return area
