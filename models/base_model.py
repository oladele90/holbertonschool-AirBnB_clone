#!/usr/bin/python3
"""Base class module for AirBnB"""
from uuid import uuid4
from datetime import datetime

dt_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, *args, **kwargs):
        """initialize new instance"""
        if args:
            pass
        if kwargs:
            for key, item in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    item = datetime.strptime(item, dt_format)
                if key not in ['__class__']:
                    setattr(self, key, item)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """redefine __str__()"""
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
