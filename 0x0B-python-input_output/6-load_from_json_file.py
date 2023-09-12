#!/usr/bin/python3
'''This module contains the load_from_json_file() function implementation'''
import json


def load_from_json_file(filename):
    '''Creates a Python Object from a JSON file"

    Arguments:
        filename: the text file name

    Returns:
        The Python Object
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        json_repr = f.read()
        return json.loads(json_repr)
