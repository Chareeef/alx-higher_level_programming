#!/usr/bin/python3
'''This module contains the implementation of add_attribute() function'''


def add_attribute(cls, name, value):
    '''adds a new attribute to an object if it’s possible'''

    if hasattr(cls, '__slots__') and name not in cls.__slots__:
        raise TypeError("can't add new attribute")
    elif isinstance(cls, (int, float, str, tuple))\
            or not hasattr(cls, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(cls, name, value)
