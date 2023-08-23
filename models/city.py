#!/usr/bin/python3
# contributor: Kevin Yeff Espinoza Salguedo

"""New class City"""

from .base_model import BaseModel


class City(BaseModel):
    """This class inherits from main/base
    BaseModel() class and has the following 
    public class attributes"""

    state_id = ""
    name = ""
