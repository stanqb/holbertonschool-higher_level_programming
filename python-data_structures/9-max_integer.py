#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Vérifie si la liste est vide
        return None
    max_value = my_list[0]  # Initialise la valeur max avec le premier élément
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
