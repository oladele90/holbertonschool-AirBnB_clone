#!/usr/bin/python3
"""Base class module for AirBnB"""
from uuid import uuid4
from datetime import datetime
from collections import OrderedDict
class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, id=None, created_at=0, updated_at=0):
        self.id = str(uuid4())
        self.created_at = str(datetime.utcnow())
        self.updated_at = str(datetime.utcnow())

    def __str__ (self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = str(datetime.utcnow())
        return self.updated_at

    def to_dict(self):
        dict1 = OrderedDict()
        dict1['__class__'] = self.__class__.__name__
        for key, item in self.__dict__.items():
                dict1[key] = item
        return dict1
