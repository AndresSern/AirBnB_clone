#!/usr/bin/python3
"""
FileStorage Class
"""
import json


class FileStorage:
    """FileStoreage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objets"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "+" + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)
        print(new_dict)

