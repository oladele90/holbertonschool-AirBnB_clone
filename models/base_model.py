#!/usr/bin/python3
"""Base class module for AirBnB"""
import uuid
import datetime

class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()
        self.created_at = datetime.fromtimestamp(time_stamp)
        self.updated_at = datetime.fromtimestamp(time_stamp)

