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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)
