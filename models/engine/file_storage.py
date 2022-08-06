#!/usr/bin/python3
""" Module for serial/unserial objects to files """
import json
import os


class FileStorage:
    """ Serialize/Deserialize python objects """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Creates a new object """
        class_name = type(obj).__name__
        my_id = obj.id
        key = class_name + "." + my_id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Saves in json format to a file """
        my_dict = {}
        for key in FileStorage.__objects:
            my_dict[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as file_path:
            json.dump(my_dict, file_path)
            file_path.close()

    def reload(self):
        """ Loads from json file """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        cls_dict = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                    "Place": Place, "Review": Review, "State": State,
                    "User": User}
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as file_path:
            objects = json.load(file_path)
            FileStorage.__objects = {}

            for key in objects:
                cls_name = key.split('.')[0]
                obj_dict = objects[key]
                FileStorage.__objects[key] = cls_dict[cls_name](**obj_dict)
