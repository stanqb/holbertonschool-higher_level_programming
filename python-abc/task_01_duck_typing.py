#!/usr/bin/python3
"""This module defines an abstract class for geometric shapes"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class defining the interface for geometric shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """Class representing a circle"""

    def __init__(self, radius):
        """Initialize a Circle with a given radius
        (ensuring non-negative value)"""
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle"""
        return (self.radius ** 2) * math.pi

    def perimeter(self):
        """Return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a given shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
