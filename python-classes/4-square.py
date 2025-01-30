#!/usr/bin/python3
"""commentaire principal"""


class Square:
    """commentaire de classe"""

    def __init__(self, size=0):
        """commentaire d'instance"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calcul de l aire"""

        return int(self.__size) ** 2

    @property
    def size(self):
        """getter pour size"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter pour size"""

        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
