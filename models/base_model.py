#!/usr/bin/python3
# contributor: Kevin Espinoza Salguedo

from uuid import uuid4
from datetime import datetime

"""Main/base Class for the project"""


class BaseModel():
    """This class will define all the common
    attributes/methods for other classes"""
    # Public instance attributes

    def __init__(self, id="", created_at=None, updated_at=None):
        """Initializing the class with the following 
        public attributes"""

        id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
