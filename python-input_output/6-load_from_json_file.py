#!/usr/bin/python3
"""Module for creating a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object loaded from the file.
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
