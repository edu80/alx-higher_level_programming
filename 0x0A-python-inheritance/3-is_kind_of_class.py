#!/usr/bin/python3
# Auth: Sangwani P Zyambo

""" This module define a function that returns True
    if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise returns False
"""


def is_kind_of_class(obj, a_class):
    """ Returns true if object is an instace of a class"""

    if isinstance(obj, a_class):
        return True
    return False
