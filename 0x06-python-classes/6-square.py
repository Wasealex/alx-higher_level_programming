#!/usr/bin/python3
"""class Square"""


class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """square initialization"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns current size of the square"""
        return (self.__size)

    @property
    def position(self):
        """returns the value of position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set and validate position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        """set and validate size"""
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
        """print square with # char to stdout"""
        if self.__size == 0:
            print("")
            return
        [print("") for x in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
