#!/usr/bin/python3
# Author: Kevin Yeff Espinoza Salguedo

"""New Class named FileStorage that will save objects to a file"""

from json import dump, load
import os
import models


class FileStorage():
    """Class that will convert the dictionary representation
    to a JSON string"""
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # Public instance methods

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """This method will set in __objects dict the
        object class name and id EX: <obj class name>.id
        we will take the example as a key format"""

        # Extracts obj class name and obj id
        # This extraction will be the key for the object
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to a JSON file"""
        dict_serialized = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        file_path = self.__file_path

        with open(file_path, "w", encoding="utf-8") as file_out:
            dump(dict_serialized, file_out, indent=2, sort_keys=True)

    def reload(self):
        """This method will deserialize the JSON file to the __objects dict
        only if the file __file_path exists, otherwise do nothing"""

        file_path = self.__file_path

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file_out:
                self.__objects = load(file_out)
                dict_deserialized = {
                    key: models.classes[value.get("__class__")](**value)
                    for key, value in self.__objects.items()
                }
                self.__objects.update(dict_deserialized)
