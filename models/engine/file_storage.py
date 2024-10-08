#!/usr/bin/python3
""" class file storage """
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes and deserialize instances to and from JSON file """
    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new = {}
        for elem in self.__objects:
            new[elem] = self.__objects[elem].to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(new, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    data = json.load(f)
                    for key, value in data.items():
                        className = value["__class__"]
                        cls = globals().get(className)
                        if cls:
                            self.__objects[key] = cls(**value)
                except Exception:
                    return
        else:
            return
