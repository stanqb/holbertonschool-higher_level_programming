#!/usr/bin/python3
"""
3-say_my_name.py

This module contains a module for print the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Check if first name and last name is a string and print this

    Parameters:
    first_name: the first name to print
    last_name: the last name to print

    Return:
    return nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
