#!/usr/bin/python3
# Auth Sangwani P Zyambo

""" Defines a class Rectangle that inherits from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Derived class that inherits from BaseGeometry base class"""

    def __init__(self, width, height):
        """instantiates class object"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
