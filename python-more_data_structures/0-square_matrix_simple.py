#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Crée une nouvelle matrice en appliquant le carré à chaque élément
    return [[x ** 2 for x in row] for row in matrix]
