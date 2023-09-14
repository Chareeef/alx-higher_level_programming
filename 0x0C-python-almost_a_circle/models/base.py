#!/usr/bin/python3
'''This module contains the base class'''


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
