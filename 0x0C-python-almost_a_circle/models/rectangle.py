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
        self.__y = value
