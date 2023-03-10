#!/usr/bin/python3
"""This module creates state class."""

from models.base_model import BaseModel

class State(BaseModel):
    """This manages instances of user class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes attributes of the class"""
        super().__init__(*args, **kwargs)
