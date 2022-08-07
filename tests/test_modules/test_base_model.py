#!/usr/bin/python3
""" Module for testing BaseModel functionality and Documentation  """
from models import base_model
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import unittest
import os
import time


class TestBaseModelMethods(unittest.TestCase):
    """ Test the BaseModel class """

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ destroys created file """
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_id_type(self):
        """ test id type """
        my_model = BaseModel()
        self.assertTrue(type(my_model.id) == str)

    def test_datetime_type(self):
        """ test datetime type """
        my_model = BaseModel()
        self.assertTrue(type(my_model.created_at) == datetime)
        self.assertTrue(type(my_model.updated_at) == datetime)

    def test_str(self):
        """ test str representation """
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id,
                                              str(my_model.__dict__))
        self.assertEqual(str(my_model), string)

    def test_id_creation(self):
        """ check for id creation """
        m1 = BaseModel()
        m2 = BaseModel()
        m3 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)
        self.assertNotEqual(m1.id, m3.id)
        self.assertNotEqual(m2.id, m3.id)

    def test_to_dict(self):
        """ Test conversion of object attributes """
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        self.assertTrue(type(my_dict["created_at"]) == str)
        self.assertTrue(type(my_dict["updated_at"]) == str)
        self.assertEqual(my_dict["created_at"],
                         my_model.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"],
                         my_model.updated_at.isoformat())

    def test_base_from_dict(self):
        """ test creation of base with kwargs """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model_dict, my_new_model.to_dict())
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)
        self.assertTrue(my_model is not my_new_model)

    def test_base_from_emp_dict(self):
        """ test with an empty dictionary """
        my_dict = {}
        my_new_model = BaseModel(**my_dict)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_base_from_non_dict(self):
        """ test with a None dictionary """
        my_new_model = BaseModel(None)
        self.assertTrue(type(my_new_model.id) == str)
        self.assertTrue(type(my_new_model.created_at) == datetime)
        self.assertTrue(type(my_new_model.updated_at) == datetime)

    def test_save(self):
        """ test save method of the basemodel """
        my_new_model = BaseModel()
        previous = my_new_model.updated_at
        my_new_model.save()
        actual = my_new_model.updated_at
        self.assertTrue(actual > previous)

    def test_isintance(self):
        """ check if object is basemodel instance """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_executable_file(self):
        """ check if the file have permissions to execute """
        is_read_true = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/base_model.py', os.W_OK)
        is_exec_true = os.access('models/base_model.py', os.X_OK)
        self.assertTrue(is_exec_true)


if __name__ == "__main__":
    unittest.main()
