#!/usr/bin/python3
"""Module contenant la fonction save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet dans un fichier sous forme de JSON.

    Args:
        my_obj (object): L'objet à enregistrer.
        filename (str): Le nom du fichier où écrire l'objet.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
