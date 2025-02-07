class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # Récupérer l'élément suivant
        self.count += 1  # Incrémenter le compteur
        return item

    def get_count(self):
        return self.count
