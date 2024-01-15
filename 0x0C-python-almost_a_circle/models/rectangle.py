#!/usr/bin/python3
"""a module that contains one Class, Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle and its characterstics
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """instatition of Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width of the rectangle(private)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height of the rectangle(private)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x of the rectangle(private)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y of the rectangle(private)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ the area of a rectangle is width * height
        """
        return self.__width * self.__height

    def display(self):
        """ prints '#' in stdout using the width and hegiht
        """
        for y in range(self.y):
            print('')
        for h in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for w in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """string reprasatntion
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)
