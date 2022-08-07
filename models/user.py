#!/usr/bin/python3
""" Module for User Data """
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
