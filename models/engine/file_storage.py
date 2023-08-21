#!/usr/bin/python3
# Author: Kevin Yeff Espinoza Salguedo

"""New Class named FileStorage that will save objects to a file"""

from json import dump


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

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """This method serializes __objects to a JSON file"""
        dict_serialized = {}
        file_path = self.__file_path
        for key, value in self.__objects.items():
            dict_serialized[key] = value.to_dict()
        with open(file_path, "w", encoding="utf-8") as file_out:
            dump(dict_serialized, file_out, indent=2, sort_keys=True)
