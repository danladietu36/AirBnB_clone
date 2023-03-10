#!/usr/bin/python3
"""This a module for the user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """This class is for managing user objects"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """This initializes attributes of user class"""
        super().__init__(*args, **kwargs)
