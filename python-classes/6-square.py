#!/usr/bin/python3
"""Module 6-square: Definition of the Square class.

This module class Square that defines a square by: (based on 5-square.py)

"""


class Square:
    """Square with size

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        give the size
        """
        self.size = size
        self.position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        give the area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        give the size of the square
        """
        return (self.__size)

    @property
    def position(self):
        """
        give the positon
        """
        return (self.__position)

    @size.setter
    def size(self, size):
        """
        set the size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @position.setter
    def position(self, position):
        """
        set the position
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(n, int) and n >= 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        print the square
        """
        if self.size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
