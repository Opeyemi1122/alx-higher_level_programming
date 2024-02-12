#!/usr/bin/python3
"""Base: super class defined"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """assigns self.id to id, if id is not None"""
            self.id = id
        else:
            """increments __nb_objects"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects