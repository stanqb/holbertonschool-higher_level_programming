# Structures de Données en Python

## Description
Ce projet est une introduction pratique aux structures de données en Python, notamment les listes, les tuples et les matrices. À travers une série d'exercices, nous explorons les manipulations fondamentales de ces structures de données.

## Environnement de Développement
- **Système d'exploitation:** Ubuntu 20.04 LTS
- **Version Python:** Python 3.8.5
- **Style de code:** pycodestyle (version 2.7.*)
- **Éditeurs autorisés:** vi, vim, emacs

## Configuration des Fichiers
- Tous les fichiers doivent commencer par `#!/usr/bin/python3`
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Tous les fichiers doivent être exécutables
- Le code doit suivre les règles de style pycodestyle

## Exercices

### 0. Affichage d'une liste d'entiers
- Fonction : `print_list_integer(my_list=[])`
- Affiche tous les entiers d'une liste, un par ligne

### 1. Accès sécurisé à un élément
- Fonction : `element_at(my_list, idx)`
- Récupère un élément à un index spécifique
- Gestion des cas d'erreur (index négatif ou hors limites)

### 2. Remplacement d'élément
- Fonction : `replace_in_list(my_list, idx, element)`
- Remplace un élément à une position spécifique
- Retourne la liste originale si l'index est invalide

### 3. Affichage inversé
- Fonction : `print_reversed_list_integer(my_list=[])`
- Affiche tous les entiers d'une liste en ordre inverse

### 4. Copie et remplacement
- Fonction : `new_in_list(my_list, idx, element)`
- Remplace un élément sans modifier la liste originaleB

### 5. Filtrage de caractères
- Fonction : `no_c(my_string)`
- Supprime tous les caractères 'c' et 'C' d'une chaîne

### 6. Matrices
- Fonction : `print_matrix_integer(matrix=[[]])`
- Affiche une matrice d'entiers

### 7. Addition de tuples
- Fonction : `add_tuple(tuple_a=(), tuple_b=())`
- Additionne deux tuples élément par élément

### 8. Retours multiples
- Fonction : `multiple_returns(sentence)`
- Retourne la longueur d'une chaîne et son premier caractère

### 9. Maximum
- Fonction : `max_integer(my_list=[])`
- Trouve le plus grand entier d'une liste

### 10. Divisible par 2
- Fonction : `divisible_by_2(my_list=[])`
- Vérifie quels nombres sont divisibles par 2

### 11. Suppression d'élément
- Fonction : `delete_at(my_list=[], idx=0)`
- Supprime l'élément à une position spécifique

### 12. Switch
- Programme qui échange les valeurs de deux variables

## Note Importante
- L'importation de modules est interdite sauf indication contraire
- Les fonctions intégrées comme `max()` sont parfois interdites pour encourager la compréhension des algorithmes
- La gestion d'erreurs doit être faite sans utiliser try/except

## Auteur
- Stan QUEUNIEZ

## Licence
Ce projet fait partie du curriculum de Holberton School.