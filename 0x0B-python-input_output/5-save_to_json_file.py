#!/usr/bin/python3
'''This module contains the save_to_json_file() function implementation'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file, using a JSON representation

    Arguments:
        my_obj: object to be serialized
        filename: the text file name
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        json_repr = json.dumps(my_obj)
        f.write(json_repr)
