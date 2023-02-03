#!/usr/bin/python3
"""Base class module for AirBnB"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, id=None, created_at=0, updated_at=0):
        self.id = uuid.uuid4()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__ (self):
        print("[BaseModel] ({}) {}".format(self.id, self.__dict__))
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        self.update_at = datetime.utcnow()
        return self.updated_at

    