#!/usr/bin/python3
""" FileStorage instance """


from models import base_model
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
