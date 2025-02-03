# Python - Héritage

## Description
Ce projet fait partie du cursus de programmation de haut niveau à Holberton School. Il se concentre sur la compréhension et l'implémentation de l'héritage en Python, un concept fondamental de la programmation orientée objet.

## Objectifs d'apprentissage
À la fin de ce projet, vous devriez être capable d'expliquer :
- Ce qu'est une superclasse, classe de base ou classe parente
- Ce qu'est une sous-classe
- Comment lister tous les attributs et méthodes d'une classe ou d'une instance
- Quand une instance peut avoir de nouveaux attributs
- Comment hériter d'une classe
- Comment définir une classe avec plusieurs classes de base
- Quelle est la classe par défaut dont héritent toutes les classes
- Comment surcharger une méthode ou un attribut hérité de la classe de base
- Quels attributs ou méthodes sont disponibles par héritage pour les sous-classes
- Quel est le but de l'héritage
- Comment utiliser les fonctions intégrées isinstance, issubclass, type et super

## Exigences

### Python Scripts
- Éditeurs autorisés : vi, vim, emacs
- Tous les fichiers seront interprétés/compilés sur Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Tous les fichiers doivent se terminer par une nouvelle ligne
- La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`
- Le code doit utiliser le style pycodestyle (version 2.7.*)
- Tous les fichiers doivent être exécutables

### Cas de Test Python
- Tous les fichiers de test doivent être dans le dossier `tests`
- Tous les fichiers de test doivent être des fichiers texte (extension : .txt)
- Tous les tests doivent être exécutés avec la commande : `python3 -m doctest ./tests/*`
- Tous les modules doivent avoir une documentation
- Toutes les classes doivent avoir une documentation
- Toutes les fonctions doivent avoir une documentation

## Tâches du Projet

### 0. Lookup
- **Fichier:** `0-lookup.py`
- **Description:** Écrire une fonction qui retourne la liste des attributs et méthodes disponibles d'un objet
- **Prototype:** `def lookup(obj)`
- La fonction retourne un objet list
- Pas d'importation de module autorisée

### 1. My list
- **Fichier:** `1-my_list.py`, `tests/1-my_list.txt`
- **Description:** Créer une classe MyList qui hérite de la classe list
- Implémenter une méthode `print_sorted()` qui imprime la liste triée (ordre croissant)
- Tous les éléments de la liste seront de type int
- Tests requis dans le fichier tests

### 2. Exact same object
- **Fichier:** `2-is_same_class.py`
- **Description:** Écrire une fonction qui vérifie si un objet est exactement une instance d'une classe spécifiée
- **Prototype:** `def is_same_class(obj, a_class)`
- Retourne True si exact, False sinon

### 3. Same class or inherit from
- **Fichier:** `3-is_kind_of_class.py`
- **Description:** Fonction qui vérifie si un objet est une instance ou hérite d'une classe spécifiée
- **Prototype:** `def is_kind_of_class(obj, a_class)`
- Vérifie l'héritage direct et indirect

### 4. Only sub class of
- **Fichier:** `4-inherits_from.py`
- **Description:** Fonction qui vérifie si un objet est une instance d'une classe qui a hérité de la classe spécifiée
- **Prototype:** `def inherits_from(obj, a_class)`
- Ne doit retourner True que pour les sous-classes

### 5. Geometry module
- **Fichier:** `5-base_geometry.py`
- **Description:** Créer une classe vide BaseGeometry
- Classe de base pour les futures formes géométriques

### 6. Improve Geometry
- **Fichier:** `6-base_geometry.py`
- **Description:** Améliorer la classe BaseGeometry
- Ajouter une méthode `area()` qui lève une Exception
- Message d'erreur: "area() is not implemented"

### 7. Integer validator
- **Fichier:** `7-base_geometry.py`, `tests/7-base_geometry.txt`
- **Description:** Étendre BaseGeometry avec un validateur d'entiers
- Méthode `integer_validator(name, value)`
- Valide que value est un entier positif
- Tests complets requis

### 8. Rectangle
- **Fichier:** `8-rectangle.py`
- **Description:** Créer une classe Rectangle héritant de BaseGeometry
- Initialisation avec width et height privés
- Validation des attributs avec integer_validator

### 9. Full rectangle
- **Fichier:** `9-rectangle.py`
- **Description:** Étendre la classe Rectangle
- Implémenter la méthode area()
- Implémenter str() et print() pour afficher [Rectangle] width/height

### 10. Square #1
- **Fichier:** `10-square.py`
- **Description:** Créer une classe Square héritant de Rectangle
- Initialisation avec size (privé)
- Implémenter area()

### 11. Square #2
- **Fichier:** `11-square.py`
- **Description:** Améliorer la classe Square
- Modifier str() et print() pour afficher [Square] size/size
- Maintenir toutes les fonctionnalités de Rectangle

## Auteur
- Stan QUEUNIEZ

## Licence
Ce projet est réalisé dans le cadre du cursus de Holberton School.