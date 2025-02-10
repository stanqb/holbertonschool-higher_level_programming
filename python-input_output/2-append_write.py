#!/usr/bin/python3
"""
Module that contains a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and returns
    the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
