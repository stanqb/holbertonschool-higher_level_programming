#!/usr/bin/python3
"""
Module 4-inherits_from
Defines the function inherits_from that checks if an object
inherits directly or indirectly from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Returns:
        bool: True if obj inherits from a_class, but is not an instance
        of a_class itself, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
