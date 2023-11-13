#!/usr/bin/python3
"""the base class template module"""
import json
import csv


class Base:
    """a base class template representation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the base constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the static method that returns the json string representation
        of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """the static method that returns the list of the
        json string representation json_string"""
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """the class method that writes the json string representation
        of list_objs to a file"""
        if list_objs is not None:
            list_objs = [ins.to_dictionary() for ins in list_objs]
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as fle:
            fle.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """the class method that returns an instance with
        all attributes already set:"""
        from models.square import Square
        from models.rectangle import Rectangle

        if cls is Square:
            new_obj = Square(5)
        elif cls is Rectangle:
            new_obj = Rectangle(1, 5)
        else:
            new_obj = None
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """the class method that returns a list of instances"""
        import os
        fle = f"{cls.__name__}.json"
        if not os.path.isfile(fle):
            return []
        with open(fle, 'r', encoding='utf-8') as fl:
            return [cls.create(**dic_)
                    for dic_ in cls.from_json_string(fl.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """the class method that saves the instancees to a csv file"""
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[ins.id, ins.width, ins.height, ins.x, ins.y]
                             for ins in list_objs]
            else:
                list_objs = [[ins.id, ins.size, ins.x, ins.y]
                             for ins in list_objs]
        with open(f"{cls.__name__}.csv", 'w', newline='',
                  encoding='utf-8') as fle:
            wrt = csv.writer(fle)
            wrt.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """the class method that loads instances from a csv file"""
        from models.rectangle import Rectangle
        from models.square import Square

        rect_lst = []
        with open(f"{cls.__name__}.csv", 'r', newline='',
                  encoding='utf-8') as fle:
            readr = csv.reader(fle)
            for rw in readr:
                rw = [int(r_) for r_ in rw]
                if cls is Rectangle:
                    dic_ = {"id": rw[0], "width": rw[1], "height": rw[2],
                            "x": rw[3], "y": rw[4]}
                else:
                    dic_ = {"id": rw[0], "size": rw[1], "x": rw[2], "y": rw[3]}
                rect_lst.append(cls.create(**dic_))

        return rect_lst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """the static method that opens a window and
        draws all the Rectangles and Squares"""
        import turtle
        import time
        import random
        screen = turtle.Screen()
        screen.colormode(255)
        for nm in list_rectangles + list_squares:
            drw = turtle.Turtle()
            drw.color((random.randrange(255), random.randrange(255),
                      random.randrange(255)))
            drw.pensize(1)
            drw.penup()
            drw.pendown()
            drw.setpos((nm.x + drw.pos()[0], nm.y - drw.pos()[1]))
            drw.pensize(10)
            drw.forward(nm.width)
            drw.left(90)
            drw.forward(nm.height)
            drw.left(90)
            drw.forward(nm.width)
            drw.left(90)
            drw.forward(nm.height)
            drw.left(90)
            drw.end_fill()

        time.sleep(5)
