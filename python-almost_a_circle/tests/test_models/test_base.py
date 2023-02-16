#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
import os

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls, class_name=Base, **kwargs):
        print(f"SetUp base")
        cls._class_name = class_name
        cls._kwargs = kwargs

    def test_instance(self):
        init_id = self._class_name(**self._kwargs).id
        first_obj = self._class_name(**self._kwargs)
        second_obj = self._class_name(**self._kwargs)
        third_obj = self._class_name(id=89, **self._kwargs)
        fourth_obj = self._class_name(id=56, **self._kwargs)
        fifth_obj = self._class_name(id='a', **self._kwargs)

        self.assertEqual(first_obj.id, init_id + 1)
        self.assertEqual(second_obj.id, first_obj.id + 1)
        self.assertEqual(third_obj.id, 89)
        self.assertEqual(fourth_obj.id, 56)
        self.assertEqual(fifth_obj.id, 'a')

    # def test_to_json(self):
    #     raise NotImplemented

    # def test_from_json(self):
    #     raise NotImplemented

    def test_save_to_file(self):
        obj = self._class_name(**self._kwargs)
        # first_obj = self.assertEqual(id=89)
        # try:
            # Is there a problem with Base.json file path ?
            # Yours tests run for Base, Rectangle, Square ...
        #filename = f"{self._class_name.__name__}.json"
        # print(f"Checking if {filename} exists...")
        #self._class_name.save_to_file([first_obj])
        #self.assertEqual(os.path.exists(f"{filename}"), True)
        #print(os.getcwd())
        #print(f"{filename}")
        print(f"Object: {obj}")
        #os.remove(f"{filename}")
        
        # except:
        #     self.assertEqual(os.path.exists(f"{self._class_name.__name__}.json"), False)
        #     self._class_name.save_to_file([first_obj])
        #     with open(f"{self._class_name.__name__}.json", "r") as f:
        #         self.assertTrue(f.read())
        # Alina could you test it ?
