#!/usr/bin/python3
"""
This is the base model that contains serial/deserial information
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """ Define all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initializes the instances attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            key_dict = kwargs.copy()
            del key_dict["__class__"]
            for key in key_dict:
                if key == "created_at" or key == "updated_at":
                    key_dict[key] = datetime.strptime(key_dict[key],
                                                      date_format)

            self.__dict__ = key_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Return string representation of the instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates updated_at """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dict with a new extra field __class__ """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()

        return new_dict
