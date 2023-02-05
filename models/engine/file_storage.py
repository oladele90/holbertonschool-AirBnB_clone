#!/usr/bin/python3
from json import dump, load, dumps
from os.path import exists
from models.base_model import BaseModel
import models


class FileStorage:
    """class for serialization and deserilization"""

    __file_path = "file.json"

    __objects = {}

    def all(self):
        """returns a dictionary representation of object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets object with key"""
        class_id = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[class_id] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            dump(to_json, file)

    def reload(self):
        """deserializes JSON file to __objects"""
        dict_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as file:
                dict_obj = load(file)
                for key, value in dict_obj.items():
                    class_nam = key.split(".")[0]
                    FileStorage.__objects[key] = eval(class_nam)(**value)
