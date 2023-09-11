#!/usr/bin/python3
'''This module contains the BaseGeometry class - task 7'''


class BaseGeometry():
    '''An BaseGeometry class

    Methods:
        area(self)
        integer_validator(self, name, value):
    '''

    def area(self):
        '''Not implemented yet. It raises an Exception'''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validate a passed value to be an integer greater or equal than 1'''

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')