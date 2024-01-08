#!/usr/bin/python3
"""a module containing class BaseGeometry
"""


class BaseGeometry:
    """
    A class with public attribute area
    """
    def area(self):
        """
        rase an exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise an exception if value is not an integer and less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
