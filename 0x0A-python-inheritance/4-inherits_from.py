#!/usr/bin/python3
"""inherits_from: function to run obj and a_class"""


def inherits_from(obj, a_class):
    """returns true or false if instance of an object is inherited"""
    #return(issubclass(type(obj), a_class) and type(obj) != a_class)
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
