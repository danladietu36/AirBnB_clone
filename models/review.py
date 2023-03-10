#!/usr/bin/python3
"""This module creates the review class."""

from model.base_model import BaseModel

class Review(BaseModel):
    """This class manages the review objects"""

    user_id = ""
    place_id = ""
    text = ""

def __init__(self, *args, **kwargs):
    """This initializes the attributes or fields for review class."""
    super().__init__(*args, **kwargs)
