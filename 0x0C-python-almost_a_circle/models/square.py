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

    def update(self, *args, **kwargs):
        """updates values of square
        """
        if args and len(args) != 0:
            ar = 0
            for arg in args:
                if ar == 0 and arg is not None:
                    self.id = arg
                elif ar == 1:
                    self.size = arg
                elif ar == 2:
                    self.x = arg
                elif ar == 3:
                    self.y = arg
                ar += 1

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """string representation of class Square
        """
        return "[Square] ({}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def to_dictionary(self):
        """dictionary reprasantation for key_value of class Square
        """
        return {"id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y}
