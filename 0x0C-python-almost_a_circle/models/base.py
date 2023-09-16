#!/usr/bin/python3
'''This module contains the Base class'''
import json


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
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file'''

        filename = cls.__name__ + '.json'

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))
