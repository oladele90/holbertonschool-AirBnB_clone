#!/usr/bin/python3
"""tests for base.py"""
import unittest
from models.base_model import BaseModel



class Test(unittest.TestCase):
    """unit tests"""

    def test_non(self):
        base1 = BaseModel(None)
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)


if __name__ == '__main__':
    unittest.main()