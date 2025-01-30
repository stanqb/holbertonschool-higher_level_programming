#!/usr/bin/python3

class Square:
    """Define a square by its size"""

    def __init__(self, size=0):
        """Initialize the square with a size"""
        self.size = size

    @property
    def size(self):
        """Get the value of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the size, with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
