#!/usr/bin/python3
"""Base class module for AirBnB"""
import uuid


class BaseModel:
    """Base class for AirBnB project"""

    def __init__(self, id, created_at, updated_at):
        self.id = uuid.uuid4()