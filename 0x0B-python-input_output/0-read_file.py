#!/usr/bin/python3
'''This module contains the read_file() function implementation'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
