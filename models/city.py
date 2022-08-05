#!/usr/bin/python3
""" Module for City data """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class City that inherities from BaseModel """
    state_id = ""
    name = ""
