#!/usr/bin/python3
"""This is the "4-print_square" module.
The example module supplies one function, print_square().  For example,
>>> print_square(matrix, 3)
###
###
###"""


def print_square(size=1):
    """prints a square with the character #.
    The size of the character must be an integer
    and greater than 0"""

    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
        
