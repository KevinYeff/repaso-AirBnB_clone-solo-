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

    def test_init_equal(self):
        """Testing if the initial attributes are equal or not when a new
        obj is created or updated"""

        initial_id = self.my_model_base.id
        initial_created_at = self.my_model_base.created_at
        initial_updated_at = self.my_model_base.updated_at
        self.my_model_base.save()

        self.assertEqual(self.my_model_base.id, initial_id)
        self.assertEqual(self.my_model_base.created_at, initial_created_at)
        self.assertEqual(self.my_model_base.updated_at, initial_updated_at)

    def test_str_method(self):
        """Testing the __str__() method from BaseModel"""
        initial_string = self.my_model_base.__str__()
        self.assertIsNotNone(initial_string)
        self.assertIs(type(initial_string), str)
        self.assertTrue(type(initial_string), str)
        att_to_check = ["id", "created_at",
                        "updated_at", "[BaseModel]"]
        for att in att_to_check:
            self.assertIn(att, att_to_check)

    def test_save_method(self):
        """Testing the save() method from BaseModel"""

        self.assertIsNotNone(self.my_model_base.updated_at)
        initial_updated_at = self.my_model_base.updated_at
        self.assertEqual(self.my_model_base.created_at,
                         self.my_model_base.updated_at)
        self.my_model_base.newInt = 1
        self.my_model_base.save()
        self.assertIsNotNone(self.my_model_base.updated_at)
        self.my_model_base.newFloat = 2.5
        self.my_model_base.save()
        self.assertEqual(self.my_model_base.updated_at, initial_updated_at)
        self.assertEqual(self.my_model_base.created_at,
                         self.my_model_base.updated_at)

    def test_to_dict_method(self):
        """Testing the to_dict() method from BaseModel"""
        saving_dict = self.my_model_base.to_dict()
        self.assertIsNotNone(saving_dict)
        self.assertIs(type(saving_dict), dict)
