#!/usr/bin/python3
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .state import State

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State
}

storage = FileStorage()
storage.reload()
