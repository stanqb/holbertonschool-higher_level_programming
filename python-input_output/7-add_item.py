#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
then saves them to a JSON file.
"""

import os
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

if __name__ == "__main__":
    # Vérifier si fichier existe et charger son contenu, sinon créer une l vide
    if os.path.isfile(filename):
        try:
            my_list = load_from_json_file(filename)
        except ValueError:  # Gérer le cas où le fichier JSON est corrompu
            my_list = []
    else:
        my_list = []

    # Ajouter les nouveaux arguments à la liste
    my_list.extend(sys.argv[1:])

    # Sauvegarder la liste mise à jour dans le fichier
    save_to_json_file(my_list, filename)
