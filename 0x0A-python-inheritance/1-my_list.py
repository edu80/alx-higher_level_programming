#!/usr/bin/python3
# Auth: Sangwani P Zyambo
""" This module defines a class Mylist that inherits from 'list'"""


class MyList(list):
    """ inherits from the list base class and implements
        sorted printing
    """

    def print_sorted(self):
        """ prints the list sorted in ascending order """
        print(sorted(self))
