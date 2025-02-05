#!/usr/bin/python3
"""
Module contenant la fonction lookup
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    Args:
        obj (any): L'objet dont on veut récupérer les attributs et méthodes.

    Returns:
        list: Liste des attributs et méthodes disponibles.
    """
    return dir(obj)
