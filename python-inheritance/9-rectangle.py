#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
