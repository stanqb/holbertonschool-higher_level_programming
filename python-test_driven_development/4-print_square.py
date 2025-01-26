#!/usr/bin/python3

"""
Module for print_square function
"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size (int): size of the square

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size <= 0:
        raise ValueError("size must be >= 0")

    for index in range(0, size):
        for index in range(0, size):
            print("#", end="")
        print("")

        
