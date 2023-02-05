#!/usr/bin/python3
"""tests for base.py"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class Test(unittest.TestCase):
    """unit tests"""

    def test_id(self):
        base1 = BaseModel(None)
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_type(self):
        base1 = BaseModel()
        self.assertIsInstance(base1.id, str)
        self.assertIsInstance(base1.created_at, datetime)
        self.assertIsInstance(base1.updated_at, datetime)

    def test_save(self):
        base1 = BaseModel()
        update1 = base1.updated_at
        base1.save()
        self.assertNotEqual(update1, base1.updated_at)

    def test_to_dict(self):
        base1 = BaseModel()
        dict1 = base1.to_dict()
        self.assertIsInstance(dict1, dict)
        self.assertIsInstance(dict1["created_at"], str)
        self.assertIsInstance(dict1["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
