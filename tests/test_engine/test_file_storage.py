#!/usr/bin/python3
"""tests for file_storage.py"""
from datetime import datetime
import unittest
from models.base_model import BaseModel as BaseModel
from models.engine.file_storage import FileStorage as FileStorage


class Test(unittest.TestCase):
    """creates class of unittests"""

    def test_type(self):
        """test types of object and file path"""
        storage = FileStorage()
        self.assertIsNotNone(storage)
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_all(self):
        """test all function"""
        storage = FileStorage()
        self.assertIsNotNone(storage.all())

    def test_new(self):
        """test new function"""
        storage = FileStorage()
        base1 = BaseModel()
        storage.new(base1)
        key = f'BaseModel.{base1.id}'
        self.assertIsNotNone(storage.all(), {key: base1})

    def test_save():
        """test save function"""
        pass

    def test_reload():
        """test reload function"""
        pass


if __name__ == '__main__':
    unittest.main()
