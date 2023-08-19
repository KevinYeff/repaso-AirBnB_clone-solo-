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

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Class method that prints the class name and id
        to a dictionary
        Ex: [<class name>] (<self.id>) <self.__dict__>"""
        return (f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}")

    """Public instance methods"""

    def save(self):
        """Public instance method that updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
