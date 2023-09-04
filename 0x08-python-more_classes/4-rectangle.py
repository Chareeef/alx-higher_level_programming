#!/usr/bin/python3
'''
This module creates a Rectangle class
with useful attributes and methods
'''


class Rectangle():
    '''A Rectangle class'''

    def __init__(self, width=0, height=0):
        '''Initialize a Rectangle instance

        Args:
            width (int): set by default to 0
            height (int): set by default to 0

        Raises:
            TypeError: in one of the dimensions is not int
            ValueError: in one of the dimensions is negative
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter and Setter for the `__width` attribute'''

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter and Setter for the `__height` attribute'''
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Return the rectangle area'''

        return self.height * self.width

    def perimeter(self):
        '''Return the rectangle perimeter'''

        if 0 in (self.height, self.width):
            return 0
        else:
            return (self.height + self.width) * 2

    def __str__(self):

        if 0 in (self.height, self.width):
            return ''

        rect_str = ''
        for n in range(self.height):
            rect_str += '#' * self.width
            if n < self.height - 1:
                rect_str += '\n'

        return rect_str

    def __repr__(self):

        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
