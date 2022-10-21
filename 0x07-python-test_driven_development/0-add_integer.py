#!/usr/bin/python3
"""This module contain a function that add two integers
Args:
    a (int): first parameter
    b (int): second parameter
"""


def add_integer(a, b=98):
    """add_integer function that add two integers
    Returns:
        int: Addition between a + b."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
