#!/usr/bin/python3
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.base_model import BaseModel
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as f:
                    self.__objects = json.load(f)
            except:
                pass