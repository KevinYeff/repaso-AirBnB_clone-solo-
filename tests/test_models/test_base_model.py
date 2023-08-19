#!/usr/bin/python3
# Author: Kevin Espinoza Salguedo
# git username: KevinYeff
# e-mail: kevinyeff94@gmail.com

"""Unit testing"""

import unittest
from models.base_model import BaseModel
from uuid import uuid4
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

        # self.my_model_base = BaseModel()
        self.custom_id = str(uuid4())
        self.custom_created_at = datetime.now().isoformat()
        self.custom_updated_at = datetime.now().isoformat()
        self.initial_dict_att = {
            "id": self.custom_id,
            "created_at": self.custom_created_at,
            "updated_at": self.custom_updated_at
        }

        self.my_model_form_dict = BaseModel(**self.initial_dict_att)

    def tearDown(self):
        """This module is used for cleaning the environment """
        # del self.my_model
        del self.my_model_form_dict

    def test_init_instance(self):
        """This module tests the initial BaseModel class"""
        self.assertIsNot(self.my_model_form_dict.id, self.custom_id)
        self.assertNotEqual(self.my_model_form_dict.created_at,
                            self.custom_created_at)
        self.assertNotEqual(self.my_model_form_dict.updated_at,
                            self.custom_updated_at)
        self.assertFalse(hasattr(self.my_model_form_dict, "custom_extra_att"))
