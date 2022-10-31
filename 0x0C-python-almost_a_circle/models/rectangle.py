#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))

    @property
    def width(self):
        """ Property of width """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Property of height """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ property of x """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ property of y """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Area of rectangle """
        return (self.__height * self.__width)

    def display(self):
        """ print the Rectangule  width, height, x, y, id"""
        for y in range(0, self.__y):
            print()
        for line in range(0, self.__height):
            for x in range(0, self.x):
                print(" ", end="")
            for colum in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ method to update the instances of object """
        lista = ['id', 'width', 'height', 'x', 'y']
        if args is None or len(args) is 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for x in range(0, len(args)):
                setattr(self, lista[x], args[x])

    def to_dictionary(self):
        """ Dictionary representatios of object """
        dic = {}
        lista = ['id', 'width', 'height', 'x', 'y']
        for x in lista:
            dic[x] = getattr(self, x)
        return dic
