#!/usr/bin/python3
'''This module contains the Square class - task 8'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A Square class

    Attributes:
        __size (positive integer)

    Methods:
        area(self)
    '''

    def __init__(self, size):

        self.integer_validator('size', size)

        self.__size = size

    def area(self):
        '''Returns the Square's area'''

        return self.__size ** 2
