#!/usr/bin/python3
"""class Square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """square initialization"""
        self.size = size

    @property
    def size(self):
        """returns current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """validating size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square to stdout in # character"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
