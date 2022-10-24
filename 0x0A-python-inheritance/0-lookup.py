#!/usr/bin/python3
# Auth: Sangwani P Zyambo:
""" this module contains a function that
    returns all attributes and methods of an object
"""


def lookup(obj):
    """ return all available
        attributes and methods an object
        param: obj(object) - object to get attribtes and methods from.
    """
    return dir(obj)
