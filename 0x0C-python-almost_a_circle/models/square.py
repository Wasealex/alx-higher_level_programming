#!/usr/bin/python3
"""a module that contains one class, Square()
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that contains its attribute of square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """inistantion of class Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size from rectangle one side
        """
        return self.width

    @size.setter
    def size(self, value):
        """set size a value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of class Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)
