#!/usr/bin/python3
"""Test City"""

import os
import pep8
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test"""

    def test_style(self):
        """Style"""
        style = pep8.StyleGuide(quit=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def has_attributes(self):
        """Attributes"""
        c = City()
        self.asserTrue('id' in self.c.__dict__)
        self.assertTure('created_at' in self.c.__dict__)
        self.assertTrue('updated_at' in self.c.__dict__)
        self.assertTrue('state_id' in self.c.__dict__)
        self.assertTrue('name' in self.c.__dict__)

    def attr_are_str(self):
        """Attributes"""
        c = City()
        self.assertEqual(type(self.c.name), str)
        self.assertEqual(type(selc.c.state_id), str)

    def is_subclass(self):
        """Subclass"""
        c = City()
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def to_dict(self):
        """Dict"""
        self.assertEqual('to_dict' in dir(self.city1), True)

    def check_funcitons(self):
        """Functions"""


if __name__ == '__main__':
    unittest.main()
