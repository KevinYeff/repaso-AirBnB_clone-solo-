#!/usr/bin/python3
# Author: Kevin Yeff Espinoza Salguedo

"""New Class named FileStorage that will save objects to a file"""


class FileStorage():
    """Class that will convert the dictionary representation
    to a JSON string"""
    # Private class attributes
    __file_path = "file.json"
    __objects = {}
