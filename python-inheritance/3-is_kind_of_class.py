#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines the function is_kind_of_class that checks if an object
is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of, or if it inherits from a_class.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Returns:
        bool: True if obj is an instance of, or inherits from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
