#!/usr/bin/python3
""" Module for Review data model """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review that inherities from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
