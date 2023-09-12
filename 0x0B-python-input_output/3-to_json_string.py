#!/usr/bin/python3
'''This module contains the to_json_string() function implementation'''
import json


def to_json_string(obj):
    ''' Returns the JSON representation of an object

    Arguments:
        obj: object to be serialized

    Returns:
        The JSON representation (string)
    '''

    return json.dumps(obj)
