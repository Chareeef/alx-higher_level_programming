#!/usr/bin/python3
'''Write a class Square that defines a square by:
Private instance attribute: size
Instantiation with optional size (with type and value verifications)
Public instance method: def area(self): that returns the current square area'''


class Square:
    '''A Square with 'size' as private instance attr. and 'area' method'''

    def __init__(self, size=0):
        '''Initialize Square class with 'size' as private instance attribute
        After performing type and value verifications'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Returns the square area'''
        return self.__size ** 2
