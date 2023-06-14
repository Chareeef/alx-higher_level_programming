#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or len(a_dictionary) == 0:
        return a_dictionary
    items = list(a_dictionary.items())
    for key, val in items:
        if value == val:
            del a_dictionary[key]
    return a_dictionary
