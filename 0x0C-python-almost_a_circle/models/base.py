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
        dicts = []
        if type(list_objs) is list:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def load_from_file(cls):
        '''That returns a list of instances from a JSON in a file'''

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
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''

        inst = cls(1, 1)

        inst.update(**dictionary)

        return inst
