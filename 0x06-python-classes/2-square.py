#!/usr/bin/python3
'''Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with optional size (with type and value verifications)'''


class Square:
    '''A Square class with 'size' as private instance attribute'''
    def __init__(self, size=0):
        '''Initialize Square class with 'size' as private instance attribute
        After performing type and value verifications'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
