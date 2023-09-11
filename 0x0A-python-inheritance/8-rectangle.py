#!/usr/bin/python3
'''This module contains the Rectangle class - task 8'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A Rectangle class

    Attributes:
        __height (positive integer)
        __width (positive integer)
    '''

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
