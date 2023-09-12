#!/usr/bin/python3
'''This module contains the Student class'''


class Student:
    '''A Student class

    Attributes:
        first_name (str)
        last_name (str)
        age (int)

    Methods:
        to_json(self)
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return a dictionary description of the instance
        If `attrs` is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        '''
        if type(attrs) is not list:
            return self.__dict__

        # Ensure that 'attrs' is a list containing strings
        for i in range(len(attrs)):
            if type(attrs[i]) is str:
                break
            if i == len(attr) - 1:
                return self.__dict__

        json_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                json_dict[key] = value

        return json_dict
