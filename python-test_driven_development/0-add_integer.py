#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    If either a or b is a float, they are casted to integers.
    Raises TypeError if a or b is not an integer or a float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
