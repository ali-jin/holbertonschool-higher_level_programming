#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase,):
    @classmethod
    def setUpClass(cls, class_name=Base, **kwargs):
        cls._class_name = class_name

    def TestInstance(self):
        init_id = self._class_name().id
        first_obj = self._class_name()
        second_obj = self._class_name()
        third_obj = self._class_name(89)
        fourth_obj = self._class_name(56)
        fifth_obj = self._class_name('a')

        self.assertEqual(first_obj.id, init_id + 1)
        self.assertEqual(second_obj.id, first_obj.id + 1)
        self.assertEqual(third_obj.id, 89)
        self.assertEqual(fourth_obj.id, 56)
        self.assertEqual(fifth_obj.id, 'a')