#!/usr/bin/python3
'''This module contains the Rectangle class - task 8'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class

    Attributes:
        __height (positive integer)
        __width (positive integer)

    Methods:
        area(self)
    '''

    def __init__(self, width, height):

        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        '''Returns the Rectangle's area'''

        return self.__height * self.__width

    def __str__(self):
        '''Return the dimensions representation of the Rectangle'''

        return f"[Rectangle] {self.__width}/{self.__height}"
