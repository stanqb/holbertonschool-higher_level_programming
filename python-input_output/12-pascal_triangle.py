#!/usr/bin/python3
"""A module that generates Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists containing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialisation avec la première ligne

    for i in range(1, n):
        row = [1]  # Chaque ligne commence par 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Chaque ligne finit par 1
        triangle.append(row)

    return triangle
