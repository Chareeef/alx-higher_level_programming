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

    def to_json(self):
        '''Return a dictionary description of the instance'''
        return self.__dict__
