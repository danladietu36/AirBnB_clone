#!/usr/bin/python3
"""This module ceates the amenity class"""

from model.base_model import BaseModel

class Amenity(BaseModel):
    """This is the amenity class that inherits from the BaseModel class, it manages amenity objects."""

    def __init__(self, *args, **kwargs):
        """This initializes the amenity class"""
        super().__init__(*args, **kwargs)
