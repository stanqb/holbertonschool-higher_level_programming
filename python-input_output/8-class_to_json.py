#!/usr/bin/python3
"""
Module that contains the function class_to_json
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        dict: A dictionary containing all serializable attributes
    """
    return obj.__dict__
