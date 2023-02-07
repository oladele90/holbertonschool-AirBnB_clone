#!/usr/bin/python3
"""tests for file_storage.py"""
from datetime import datetime
import unittest
from models.base_model import BaseModel as BaseModel
from models.engine.file_storage import FileStorage as FileStorage


class Test(unittest.TestCase):
    """creates class of unittests"""

    def test_type(self):
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        storage = FileStorage()
        self.assertIsNotNone(storage.all())

    def test_new(self):
        storage = FileStorage()
        base1 = BaseModel()
        storage.new(base1)
        self.assertIsNotNone(storage.all())
