# Python - Modules d'importation

## Description
Ce projet explore les concepts fondamentaux des modules et des importations en Python. Il couvre l'importation de fonctions, la création de modules, et l'utilisation d'arguments en ligne de commande.

## Objectifs d'apprentissage
À la fin de ce projet, vous devriez être capable d'expliquer :
* Pourquoi la programmation Python est excellente
* Comment importer des fonctions depuis un autre fichier
* Comment utiliser les fonctions importées
* Comment créer un module
* Comment utiliser la fonction intégrée dir()
* Comment empêcher l'exécution du code lors de l'importation
* Comment utiliser les arguments de ligne de commande dans vos programmes Python

## Configuration requise
* Environnement : Ubuntu 22.04 LTS
* Python version : Python 3.10.*
* Style de code : pycodestyle (version 2.7.*)
* Éditeurs autorisés : vi, vim, emacs

## Structure des fichiers
* Tous les fichiers doivent commencer par `#!/usr/bin/python3`
* Tous les fichiers doivent être exécutables
* Tous les fichiers doivent se terminer par une nouvelle ligne

## Tâches

### 0. Importer une fonction simple
* Fichier : `0-add.py`
* Description : Programme qui importe la fonction `add(a, b)` et affiche le résultat de 1 + 2

### 1. Ma première boîte à outils
* Fichier : `1-calculation.py`
* Description : Programme qui importe des fonctions de `calculator_1.py` et effectue des opérations mathématiques

### 2. Script dynamique
* Fichier : `2-args.py`
* Description : Programme qui affiche le nombre et la liste des arguments reçus

### 3. Addition infinie
* Fichier : `3-infinite_add.py`
* Description : Programme qui additionne tous les arguments reçus

### 4. Qui es-tu ?
* Fichier : `4-hidden_discovery.py`
* Description : Programme qui affiche tous les noms définis dans le module compilé `hidden_4.pyc`

### 5. Tout peut être importé
* Fichier : `5-variable_load.py`
* Description : Programme qui importe une variable depuis un fichier et affiche sa valeur

## Utilisation
```bash
# Exemple d'exécution pour la tâche 0
./0-add.py
# Sortie attendue : 1 + 2 = 3

# Exemple d'exécution pour la tâche 2
./2-args.py Hello Welcome
# Sortie attendue :
# 2 arguments:
# 1: Hello
# 2: Welcome
```

## Note importante
* Le code ne doit pas s'exécuter lors de l'importation
* Respectez les conventions de style PyCodeStyle
* Tous les fichiers seront testés sur Ubuntu 22.04 LTS