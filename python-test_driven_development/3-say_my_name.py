#!/usr/bin/python3
"""
Module 3-say_my_name

This module defines a function to print a person's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name to display.
        last_name (str): The last name to display (optional).

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Doe")
        My name is John Doe
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
