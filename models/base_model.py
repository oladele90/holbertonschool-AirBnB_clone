#!/usr/bin/python3
"""Base class module for AirBnB"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, id=None, created_at=0, updated_at=0):
        """initialize new instance"""
        self.id = str(uuid4())
        self.created_at = (datetime.utcnow())
        self.updated_at = (datetime.utcnow())

    def __str__(self):
        """redefine __str__()"""
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """save method updates timestamp"""
        self.updated_at = (datetime.utcnow())
        return self.updated_at

    def to_dict(self):
        """to_dict method converts to json rep"""
        dict1 = {}
        dict1['__class__'] = self.__class__.__name__
        for key, item in self.__dict__.items():
            dict1[key] = item
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        return dict1
