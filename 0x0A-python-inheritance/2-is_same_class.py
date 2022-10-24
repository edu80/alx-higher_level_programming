#!/usr/bin/python3
# Auth: Sangwani P Zyambo

"""
    Defines a function that returns True if an object is
    exactly an instance of the specified class; otherwise false.
"""


def is_same_class(obj, a_class):
    """ return True if obj is instance of a_class
        otherwise return False
    """
    if type(obj) == a_class:
        return True
    return False
