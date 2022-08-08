#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models import user
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """TestUserClass resume
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """Return to "" class attributes"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)

    def test_email(self):
        """ test that user has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")


if __name__ == '__main__':
    unittest.main()
