# Projet de Sérialisation Python

## Description
Ce projet explore les concepts fondamentaux de la sérialisation et du marshaling en Python. Il permet de comprendre comment les données peuvent être transformées et communiquées entre différentes parties d'un système ou entre différents systèmes.

## Concepts Clés
- **Marshaling** : Processus de transformation d'objets en mémoire vers un format pouvant être stocké ou transmis sur un réseau.
- **Sérialisation** : Conversion de structures de données ou d'états d'objets dans un format facilement sauvegardable ou transmissible.

## Objectifs d'Apprentissage
- Comprendre les différences et similitudes entre marshaling et sérialisation
- Implémenter la sérialisation dans des tâches pratiques
- Maîtriser l'utilisation des données sérialisées dans les applications web, bases de données et communications réseau
- Évaluer les implications de performance des différents formats de sérialisation

## Structure du Projet

### 0. Sérialisation Basique
**Fichier** : `task_00_basic_serialization.py`

Implémente deux fonctions principales :
- `serialize_and_save_to_file(data, filename)` : Sérialise un dictionnaire Python en fichier JSON
- `load_and_deserialize(filename)` : Désérialise un fichier JSON en dictionnaire Python

### 1. Pickling de Classes Personnalisées
**Fichier** : `task_01_pickle.py`

Crée une classe `CustomObject` avec :
- Attributs : nom, âge, statut étudiant
- Méthodes :
  - `serialize(filename)` : Sérialise l'instance
  - `deserialize(filename)` : Désérialise et retourne une instance
  - `display()` : Affiche les attributs

### 2. Conversion CSV vers JSON
**Fichier** : `task_02_csv.py`

Implémente la fonction `convert_csv_to_json` qui :
- Lit un fichier CSV
- Convertit les données en format JSON
- Sauvegarde dans 'data.json'

### 3. Sérialisation XML
**Fichier** : `task_03_xml.py`

Contient deux fonctions principales :
- `serialize_to_xml(dictionary, filename)` : Convertit un dictionnaire en XML
- `deserialize_from_xml(filename)` : Lit un XML et retourne un dictionnaire

## Installation et Prérequis
```bash
git clone https://github.com/[votre-username]/holbertonschool-higher_level_programming.git
cd python-serialization
```

## Utilisation

### Exemple de Sérialisation Basique
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data, 'data.json')
result = load_and_deserialize('data.json')
```

### Exemple de Pickling
```python
from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
```

### Exemple de Conversion CSV
```python
from task_02_csv import convert_csv_to_json

convert_csv_to_json("data.csv")
```

### Exemple de Sérialisation XML
```python
from task_03_xml import serialize_to_xml, deserialize_from_xml

data = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

serialize_to_xml(data, "data.xml")
result = deserialize_from_xml("data.xml")
```

## Auteur
- Stan QUEUNIEZ

## Licence
Ce projet est réalisé dans le cadre du cursus Holberton School.