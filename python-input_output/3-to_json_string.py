#!/usr/bin/python3
"""
Module that contains a function to convert an object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to serialize.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
