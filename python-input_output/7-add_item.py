#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Charger la liste existante ou en créer une vide
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Ajouter les nouveaux arguments à la liste
my_list.extend(sys.argv[1:])

# Sauvegarder la liste mise à jour dans le fichier
save_to_json_file(my_list, filename)
