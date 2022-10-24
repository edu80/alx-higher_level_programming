#!/usr/bin/python3
# Sangwani P Zyambo

""" defines a class MyInt that inherits from int
    and overloads the == and != operators.
"""


class MyInt(int):
    """overloads the == and != operators """

    def __eq__(self, num):
        """ return False if equal"""
        return self.real != num

    def __ne__(self, num):
        """ return True if equal"""
        return self.real == num
