#!/usr/bin/python3
"""Initializes the package"""
#from models.base_model import BaseModel
from models.engine import file_storage

__all__ = ["city.py", "place.py", "amenity.py", "review.py", "state.py", "user.py", "base_model.py"]
storage = file_storage.FileStorage()
storage.reload()
