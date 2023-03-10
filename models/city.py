#!/usr/bin/python3
"""This a module that creates city class"""
name = ""
state_id = ""

class City(BaseModel):
    """This class manages city objects."""

    def __init__(self, *args, **kwargs):
        """Method to initialize city class"""
        super().__init__(*args, **kwargs)
