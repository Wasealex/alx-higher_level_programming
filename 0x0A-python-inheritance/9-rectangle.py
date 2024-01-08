#!/usr/bin/python3
"""contains class and subclass, BaseGeometry and Rectangle Respectively
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    represent a rectangle characterstics
    """

    def __init__(self, width, height):
        """
        instantazation of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implemented area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """informal representation of rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
