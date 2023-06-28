#!/usr/bin/python3
'''Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with size (no type/value verification)'''


class Square:
    '''A Square class with 'size' as private instance attribute'''
    def __init__(self, size):
        '''Initialize Square class with 'size' as private instance attribute'''
        self.__size = size
