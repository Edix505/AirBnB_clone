#!/usr/bin/python3
"""Implements the user's model"""
from models.base_model import BaseModel


class User(BaseModel):
    """ BaseModel class and add user's functionalities """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
