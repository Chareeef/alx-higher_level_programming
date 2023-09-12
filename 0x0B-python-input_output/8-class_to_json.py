#!/usr/bin/python3
'''This module contains the class_to_json() function implementation'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Arguments:
        obj: a class instance

    Returns:
        The dictionary description
    '''
    return obj.__dict__
