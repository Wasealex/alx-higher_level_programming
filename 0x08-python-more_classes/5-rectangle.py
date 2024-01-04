#!/usr/bin/python3
"""Rectangle characterstics defintions"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:width (int): The width of the new rectangle.
             height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle
           area is width multiplied by height
           Area = Width * Height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of a rectangle
           perimeter is the sum of all sides of rectangle
           perimeter = width + height + width + height
           if width or height is equal to 0, perimeter is equal to 0
        """
        if (self.width == 0 or self.height == 0):
            return 0
        return (self.__width + self.__height + self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character #:
            if width or height is equal to 0, returns an empty string
        """
        my_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return (my_rectangle)

        for h in range(self.__height):
            for w in range(self.__width):
                my_rectangle += '#'
            if h != self.__height - 1:
                my_rectangle += '\n'
        return my_rectangle

    def __repr__(self):
        """ representing the rectangle of the string"""

        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return (r)
