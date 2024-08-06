#!/usr/bin/python3
""" city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class inherits from base model"""
    state_id = ""
    name = ""
