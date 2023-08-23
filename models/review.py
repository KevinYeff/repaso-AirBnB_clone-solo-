#!/usr/bin/python3
# contributor: Kevin Yeff Espinoza Salguedo

"""New class Review"""

from .base_model import BaseModel


class Review(BaseModel):
    """Class that inherits from main/base
    BaseModel() class and has the following 
    public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
