#!/usr/bin/pyhton3
"""State class"""

import uuid
from datetime import datetime
from models.base_model import BaseModel

class State(BaseModel):
    """ State class """
    name = ""