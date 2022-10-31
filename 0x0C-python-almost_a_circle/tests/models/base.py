#!/usr/bin/python3
"""
Class base
"""
import json
import os
import csv
import turtle


class Base:
    """
    Class Base change id()
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dictionary python to Json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save into a file json """
        filename = (cls.__name__ + ".json")
        with open(filename, mode="w") as f:
            lis = []
            if list_objs is None:
                f.write(cls.to_json_string(lis))
            else:
                for it in range(0, len(list_objs)):
                    lis.append(list_objs[it].to_dictionary())
                f.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        """ load from json """
        if json_string is None or len(json_string) is 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Return a instance with all attr """
        if cls.__name__ == "Square":
            ret = cls(2)
        else:
            ret = cls(2, 2)
        ret.update(**dictionary)
        return ret

    @classmethod
    def load_from_file(cls):
        """ returt a list of instances """
        list_ret = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename) is False:
            return list_ret
        with open(filename, mode="r") as f:
            line = f.read()
        n_line = cls.from_json_string(line)
        for x in range(0, len(n_line)):
            list_ret.append(cls.create(**n_line[x]))
        return list_ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save into a file .csv
        """
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            csv_format = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            csv_format = ["id", "size", "x", "y"]

        with open(filename, mode="w") as data:
            writer = csv.DictWriter(data, fieldnames=csv_format)
            [writer.writerow(item.to_dictionary()) for item in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """
        load from a .csv file
        """
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename) is False:
            return []
        ret = []
        dic = {}
        if cls.__name__ == "Rectangle":
            csv_format = ['id', 'width', 'height', 'x', 'y']
        else:
            csv_format = ['id', 'size', 'x', 'y']

        with open(filename, mode="r") as fd:
            reader = csv.DictReader(fd, fieldnames=csv_format)
            for item in reader:
                for key in item:
                    dic[key] = int(item[key])
                ret.append(cls.create(**dic))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw the objects with Turtle Graphics
        """
        new_window = turtle.Screen()
        new_window.bgcolor("white")
        new_window.title("Made by Cristian Diaz")
        new_turtle = turtle.Turtle()

        for rectangle in list_rectangles:
            new_turtle.color("Violet", "blue")
            new_turtle.begin_fill()
            dic = rectangle.to_dictionary()
            new_turtle.penup()
            new_turtle.setpos(dic["x"], dic["y"])
            new_turtle.pendown()
            for x in range(0, 2):
                new_turtle.forward(dic["height"])
                new_turtle.right(90)
                new_turtle.forward(dic["width"])
                new_turtle.right(90)
            new_turtle.end_fill()

        for square in list_squares:
            new_turtle.color("Red", "Green")
            new_turtle.begin_fill()
            dic = square.to_dictionary()
            new_turtle.penup()
            new_turtle.setpos(dic["x"], dic["y"])
            new_turtle.pendown()
            for size in range(0, 4):
                new_turtle.forward(dic["size"])
                new_turtle.right(90)
            new_turtle.end_fill()
        turtle.done()
