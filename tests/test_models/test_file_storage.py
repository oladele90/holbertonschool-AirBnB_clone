#!/usr/bin/python3
"""tests for file_storage.py"""
from datetime import datetime
import unittest
from models.base_model import BaseModel as BaseModel
from models.engine.file_storage import FileStorage as FileStorage
import os


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

    def test_save(self):
        """test save function"""
        storage = FileStorage()
        base1 = BaseModel()
        storage.new(base1)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as f:
            file1 = f.read()
        self.assertTrue(len(file1) > 0)

    def test_reload(self):
        """test reload function"""
        pass


if __name__ == '__main__':
    unittest.main()
