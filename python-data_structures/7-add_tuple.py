#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Remplir les tuples avec des 0 si nécessaire
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # Additionner les deux premiers éléments de chaque tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
