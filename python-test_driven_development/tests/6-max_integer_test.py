#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertAlmostEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertAlmostEqual(max_integer([10, 4, 3, 1]), 10)
        self.assertAlmostEqual(max_integer([8, 5, -1, 4]), 8)
        self.assertAlmostEqual(max_integer([-1, -24, -5, -2]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
