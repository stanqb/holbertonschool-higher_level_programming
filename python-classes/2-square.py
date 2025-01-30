#!/usr/bin/python3
class Square:
    """
    This class defines a square with a private size attribute.
    The size attribute must be an integer and greater than or equal to 0.
    """

    def __init__(self, size=0):
        """
        Instantiates a square with an optional size.

        Arguments:
            size: Size of the square (must be an integer >= 0).

        Raises a TypeError exception if size is not an integer.
        Raises a ValueError exception if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
