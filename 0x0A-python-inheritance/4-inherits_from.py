#!/usr/bin/python3
# Auth Sanwani P Zyambo

""" This module defines a function that returns True
    if the object is an instance of a class
    that inherited(directly or indirectly) from the specified class;
    otherwise returns False.
"""


def inherits_from(obj, a_class):
    """ returns True if obj is an instance
        of a class or instance of a subclass
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
