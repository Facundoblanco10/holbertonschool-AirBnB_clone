#!/usr/bin/python3
""" testing fileStorage """

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from models import storage


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""

    def test_instances(self):
        """Check if that instances are correct"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_new(self):
        """Checking New"""
        obj = FileStorage()
        base = BaseModel()
        base.name = "Holberton"
        bmid = base.id
        storage.new(base)
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bmid])

    def test_all(self):
        """Check All"""
        base = BaseModel()
        srg = storage.all()
        self.assertIsNotNone(srg)
        self.assertEqual(srg, storage.all())
        self.assertIs(srg, storage.all())

    def test_reload(self):
        """Check Reload"""
        obj = FileStorage()
        obj.reload()
        self.assertIsNotNone(obj.all())
        self.assertIs(obj.all(), obj.all())

    def test_save_reload(self):
        """Check Save and Reload"""
        obj = FileStorage()
        base = BaseModel()
        base.name = "Holberton"
        bmid = base.id
        storage.new(base)
        storage.save()
        storage.reload()
        self.assertIsNotNone(
            storage.all()[base.__class__.__name__ + "." + bmid])

    def test_save(self):
        """Check Save"""
        filestorage = FileStorage()
        basemodel = BaseModel()
        basemodel.name = "AirBnB"
        basemodelid = basemodel.id
        storage.new(basemodel)
        storage.save()
        with open("file.json", "r") as f:
            self.assertIsNotNone(f.read())
        self.assertIsNotNone(
            storage.all()[basemodel.__class__.__name__ + "." + basemodelid])


if __name__ == '__main__':
    unittest.main()
