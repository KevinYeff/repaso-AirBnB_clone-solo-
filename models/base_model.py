#!/usr/bin/python3
# contributor: Kevin Espinoza Salguedo

from uuid import uuid4
from datetime import datetime
import models

"""Main/base Class for the project"""


class BaseModel():
    """
    This class will define all the common
    attributes/methods for other classes
    """
    # Public instance attributes

    def __init__(self, *args, **kwargs):
        """
        Initializing the instances from dict or creating a BaseModel
        class from dict, otherwise use the default public instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Class method that prints the class name and id
        to a dictionary
        Ex: [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    """Public instance methods"""

    def save(self):
        """
        Public instance method that updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key values
        of the instance
        """
        instance_dict = {
            key: value.isoformat() if key in ("created_at", "updated_at")
            else value
            for key, value in self.__dict__.items()
        }
        instance_dict.update({"__class__": self.__class__.__name__})
        return instance_dict