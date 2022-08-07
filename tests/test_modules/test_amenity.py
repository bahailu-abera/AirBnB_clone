#!/usr/bin/python3
""" Module for testing BaseModel functionality and Documentation  """
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import pep8
import unittest
import os


class TestAmenityMethods(unittest.TestCase):
    """TestAmenityClass test for the inheretit class
    Amenity, this tests that the output is as expected
    Args:
        unittest (): Propertys for unit testing
    """

    def setUp(self):
        """ condition to test file saving """
        with open("test.json", 'w'):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""

    def tearDown(self):
        """ destroys created file """
        storage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/amenity.py'
        file2 = 'tests/test_models/test_amenity.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_isintance(self):
        """ check if object is basemodel instance """
        obj = Amenity()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj, Amenity)

    def test_field_types(self):
        """ test field attributes of user """
        my_amenity = Amenity()
        self.assertTrue(type(my_amenity.name) == str)


if __name__ == "__main__":
    unittest.main()
