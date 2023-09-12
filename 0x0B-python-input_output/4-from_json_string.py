#!/usr/bin/python3
'''This module contains the from_json_string() function implementation'''
import json


def from_json_string(json_string):
    '''Returns an object (Python data structure) represented by a JSON string

    Arguments:
        json_string: JSON string to be deserialized

    Returns:
        The Python object
    '''

    return json.loads(json_string)
