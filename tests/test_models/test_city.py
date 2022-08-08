#!/usr/bin/python3
""" Module for testing BaseModel functionality and Documentation  """
from models import city
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCityMethods(unittest.TestCase):
    """TestCityClass test for the inheretit class
    City, this tests that the output is as expected
    Args:
        unittest (): Propertys for unit testing
    """

    def setUp(self):
        """Return to "" class attributes"""
        City.name = ""
        City.state_id = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_city = City()
        self.assertTrue(type(my_city.name) == str)
        self.assertTrue(type(my_city.state_id) == str)


if __name__ == "__main__":
    unittest.main()