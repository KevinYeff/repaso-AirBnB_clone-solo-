#!/usr/bin/python3
# Author: Kevin Espinoza Salguedo
# git username: KevinYeff
# e-mail: kevinyeff94@gmail.com

"""Unit testing"""

import unittest
from models.base_model import BaseModel
from uuid import UUID, uuid4
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unittest TestCase: A test case is the individual unit of testing.
    It checks for a specific response to a particular set of inputs. 
    unittest provides a base class, TestCase, which may be used to create
    new test cases.
    """

    def setUp(self):
        """This module is used for configuring the environment """

        self.my_model_base = BaseModel()

    def tearDown(self):
        """This module is used for cleaning the environment """
        del self.my_model_base
        # del self.my_model_form_dict

    def test_init_instance(self):
        """This module tests the initial BaseModel class"""

        self.assertIsInstance(self.my_model_base, BaseModel)
        # just for fun
        uuid_str = self.my_model_base.id
        uuid_obj = UUID(uuid_str)
        self.assertIsInstance(uuid_obj, UUID)
        # fun ends
        self.assertIsInstance(self.my_model_base.created_at, datetime)
        self.assertIsInstance(self.my_model_base.updated_at, datetime)

    def test_init_extra_att(self):
        """ Tests if has an extra attribute"""
        self.assertFalse(hasattr(self.my_model_base, "custom_extra_att"))

    def test_init_is(self):
        """Testing if the attributes matches the data types"""
        self.assertIs(type(self.my_model_base.id), str)
        self.assertIs(type(self.my_model_base.created_at), datetime)
        self.assertIs(type(self.my_model_base.updated_at), datetime)
