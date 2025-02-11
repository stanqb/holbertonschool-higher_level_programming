#!/usr/bin/python3
"""Module contenant la fonction from_json_string"""

import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en objet Python.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        object: L'objet Python représenté par la chaîne JSON.
    """
    return json.loads(my_str)
