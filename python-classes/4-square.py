#!/usr/bin/python3
class Square:
    """Define a Square class."""

    def __init__(self, size=0):
        """Define and initialize a square.
        size (int): the length of one side of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Define size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square.
        value (int): the new length of one side of the square
        """
        self._Square__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
