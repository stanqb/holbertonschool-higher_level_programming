#!/usr/bin/python3
"""
Module 2-is_same_class
Defines the function is_same_class that checks if an object
is an exact instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
