#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([22, -18, 9, 10]), 22)
        self.assertAlmostEqual(max_integer([9, 12, 25, 5, 2]), 25)
        self.assertAlmostEqual(max_integer([8, -2, 15, 7]), 15)
        self.assertAlmostEqual(max_integer([-1, -5, -9, -18]), -1)
        self.assertAlmostEqual(max_integer([3]), 3)
        self.assertAlmostEqual(max_integer([]), None)
