#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State
from .city import City

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City
}

storage = FileStorage()
storage.reload()
