#!/usr/bin/python3
# contributor: Kevin Espinoza Salguedo

"""First User"""

from .base_model import BaseModel


class User(BaseModel):
    """Class that inherits from the main/base class
    BaseModel() and has the following public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
