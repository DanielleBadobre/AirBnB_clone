#!/usr/bin/python3
""" a class that defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class definition """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ def str method """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ method to save instances """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ method to create dictionnary """
        newDict = self.__dict__.copy()
        newDict['__class__'] = self.__class__.__name__
        newDict['created_at'] = self.created_at.isoformat()
        newDict['updated_at'] = self.updated_at.isoformat()
        return newDict
