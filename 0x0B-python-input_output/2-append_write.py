#!/usr/bin/python3
'''This module contains the append_write() function implementation'''


def append_write(filename="", text=""):
    '''Writes a string to the end of a text file (UTF8)

    Returns:
        The number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
