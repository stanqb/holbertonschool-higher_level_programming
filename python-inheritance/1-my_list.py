#!/usr/bin/python3
"""
Module 1-my_list
Définit une classe MyList qui hérite de list et ajoute une méthode print_sorted
"""


class MyList(list):
    """
    Classe MyList qui hérite de list et ajoute une méthode pour afficher
    les éléments triés en ordre croissant.
    """

    def print_sorted(self):
        """
        Affiche la liste triée sans modifier l'instance actuelle.
        """
        print(sorted(self))
