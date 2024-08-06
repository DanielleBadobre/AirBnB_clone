#!/usr/bin/python3
""" class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ class review inherits from Base model"""
    place_id = ""
    user_id = ""
    text = ""
