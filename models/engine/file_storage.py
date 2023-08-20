#!/usr/bin/python3
# Author: Kevin Yeff Espinoza Salguedo

"""New Class named FileStorage that will save objects to a file"""


class FileStorage():
    """Class that will convert the dictionary representation
    to a JSON string"""
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # Private instance methods

    def all(self):
        """Returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """This method will set in __objects dict the 
        object class name and id EX: <obj class name>.id
        we will take the example as a key format"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
