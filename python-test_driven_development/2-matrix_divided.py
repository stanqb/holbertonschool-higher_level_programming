#!/usr/bin/python3
"""This is the "2-matrix_divided" module.
The example module supplies one function, matrix_divided().  For example,
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6]
... ]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
    all elements must be integers of floats.
    Div have to be a number different from 0"""
    col_len = len(matrix[0])
    err_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    err_2 = 'Each row of the matrix must have the same size'

    for col in matrix:
        if len(col) != col_len:
            raise TypeError(err_2)
        for row in col:
            if type(row) not in [int, float]:
                raise TypeError(err_1)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return (list(map(lambda x: list(map(lambda y: round(y / div, 2), x)),
            matrix)))
