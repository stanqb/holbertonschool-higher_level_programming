#!/usr/bin/python3
"""
Module containing a function that reads a text file and prints its content.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
