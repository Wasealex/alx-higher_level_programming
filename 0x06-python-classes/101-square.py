#!/usr/bin/python3
"""created a class named Square that adds a size as int"""


class Square:
    """initialize the class with a size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """size must be an intiger and greater than zero"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """return size of square as property"""
        return (self.__size)

    @property
    def position(self):
        """return position as private property"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """validate poistion"""
        self.__position = value
        if (type(value) != tuple or len(value) != 2
                or value[0] < 0 or value[1] < 0
                or type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def __str__(self):
        """prints # based on size given"""
        output = ""
        if self.__size == 0:
            output = output + '\n'
            return output
        for p in range(self.position[1]):
            output = output + " "
        for x in range(self.__size):
            for z in range(self.__position[0]):
                output = output + ' '
            for y in range(self.__size):
                output = output + '#'
            output = output + '\n'
        return output
