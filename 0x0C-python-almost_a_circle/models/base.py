#!/usr/bin/python3
'''This module contains the Base class'''
import json
import csv
import turtle
from time import sleep


class Base:
    '''A Base class

    Class Attributes:
        __nb_objects (int)


    Instance Attributes:
        id (int)
    '''

    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON string representation of list_dictionaries'''

        if list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list represented by json_string'''

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''

        inst = cls(1, 1)

        inst.update(**dictionary)

        return inst

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''

        filename = cls.__name__ + '.json'
        dicts = []
        if type(list_objs) is list:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def load_from_file(cls):
        '''That returns a list of instances created from a JSON in a file'''

        filename = cls.__name__ + '.json'

        try:
            list_instances = []

            with open(filename, 'r', encoding='utf-8') as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)

                for dictionary in list_dicts:
                    list_instances.append(cls.create(**dictionary))

            return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Writes the CSV string representation of list_objs to a file'''

        filename = cls.__name__ + '.csv'

        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']

        with open(filename, 'w', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            if list_objs is None or len(list_objs) == 0:
                return

            dictionaries = [obj.to_dictionary() for obj in list_objs]

            for dict_item in dictionaries:
                writer.writerow(dict_item)

    @classmethod
    def load_from_file_csv(cls):
        '''That returns a list of instances from create a CSV file'''

        filename = cls.__name__ + '.csv'

        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            fieldnames = ['id', 'size', 'x', 'y']

        list_instances = []

        try:
            with open(filename, 'r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)

                for dict_item in reader:
                    for field in fieldnames:
                        dict_item[field] = int(dict_item[field])
                    list_instances.append(cls.create(**dict_item))

            return list_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(rectangles, squares):
        '''Draw rectangles and squares using turtle module'''

        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(3)

        for r in rectangles:
            t.penup()
            t.setpos(r.x, r.y)

            t.pendown()
            t.pencolor("red")
            for _ in range(2):
                t.forward(r.height)
                t.right(90)
                t.forward(r.width)
                t.right(90)

            sleep(1)
            t.reset()

        for s in squares:
            t.penup()
            t.setpos(s.x, s.y)

            t.pendown()
            t.pencolor("blue")
            for _ in range(4):
                t.forward(s.size)
                t.right(90)

            sleep(1)
            t.reset()

        screen.exitonclick()
