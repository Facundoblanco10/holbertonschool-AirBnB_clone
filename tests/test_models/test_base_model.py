#!/usr/bin/python3
"""Test of BaseModel"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
import os
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def test_save(self):
        """Checking Save"""
        basemodel = BaseModel()
        basemodel.save()
        self.assertNotEqual(basemodel.created_at, basemodel.updated_at)

    def test__to_dict(self):
        """Check BaseModel to_dict"""
        basemodel = BaseModel()
        basemodel_dict = basemodel.to_dict()
        self.assertEqual(basemodel_dict["__class__"], "BaseModel")
        self.assertEqual(type(basemodel_dict["created_at"]), str)
        self.assertEqual(type(basemodel_dict["updated_at"]), str)
        self.assertEqual(basemodel_dict["id"], basemodel.id)
        self.assertIn("id", basemodel.to_dict())
        self.assertIn("created_at", basemodel.to_dict())
        self.assertIn("updated_at", basemodel.to_dict())
        self.assertIn("__class__", basemodel.to_dict())

    def test_string_(self):
        """Checks __str__"""
        b = BaseModel()
        self.assertEqual(f"[{type(b).__name__}] ({b.id}) {b.__dict__}", str(b))

    def test_id(self):
        """Check the ID"""
        basemodel = BaseModel()
        base_model = BaseModel()
        self.assertIsInstance(basemodel.id, str)
        self.assertNotEqual(basemodel.id, base_model.id)
        self.assertFalse(basemodel.id == base_model.id)

    def test_doc(self):
        """Check docstring"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_datetime(self):
        """Check Datetime"""
        basemodel = BaseModel()
        self.assertIsInstance(basemodel.created_at, datetime)
        self.assertIsInstance(basemodel.updated_at, datetime)

    def test_save_method(self):
        """Check Save"""
        basemodel = BaseModel()
        updated_at = basemodel.__dict__["updated_at"]
        basemodel.save()
        self.assertNotEqual(basemodel.__dict__["updated_at"], updated_at)
        self.assertTrue(os.path.isfile("file.json"))
        new_updated_at = basemodel.__dict__["updated_at"]
        storage.reload()
        self.assertEqual(basemodel.__dict__["updated_at"], new_updated_at)
        basemodel1 = BaseModel()
        updated_at = basemodel1.__dict__["updated_at"]
        basemodel1.save()
        self.assertNotEqual(basemodel1.__dict__["updated_at"], updated_at)
        self.assertTrue(os.path.isfile("file.json"))
        new_updated_at = basemodel1.__dict__["updated_at"]
        storage.reload()
        self.assertEqual(basemodel1.__dict__["updated_at"], new_updated_at)


if __name__ == '__main__':
    unittest.main()
