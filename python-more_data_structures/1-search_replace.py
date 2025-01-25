#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Crée une nouvelle liste en remplaçant les éléments correspondants
    return [replace if x == search else x for x in my_list]
