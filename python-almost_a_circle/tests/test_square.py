#!/usr/bin/python3
"""Unittest for class Square
"""
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
i
import unittest

class Testsquare(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

