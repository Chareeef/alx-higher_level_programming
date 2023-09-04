#!/usr/bin/python3
'''
This module creates a Rectangle class
with useful attributes and methods
'''


class Rectangle():
    '''A Rectangle class

    Attributes:
        height (int)
        width (int)

    Methods:
        area(self): Returns the rectangle's area
        perimeter(self): Returns the rectangle's perimeter
        bigger_or_equal(rect_1, rect_2) (staticmethod): Compare two rectangles
                                                        based on area
        square(cls, size=0) (classmethod): Returns a square of size 'síze'

    With the implemented Magic Methods:
        __str__ / __repr__ / __del__
    '''

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the biggest rectangle based on the area'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def perimeter(self):
        '''Return the rectangle perimeter'''

        if 0 in (self.height, self.width):
            return 0
        else:
            return (self.height + self.width) * 2

    @classmethod
    def square(cls, size=0):
        '''Returns a new Rectangle instance with width == height == size

        Args:
            size (int): square's array size

        Returns:
            A new Rectangle instance
        '''
        return Rectangle(size, size)

    def __str__(self):
        if 0 in (self.height, self.width):
            return ''

        rect_str = ''
        for n in range(self.height):
            rect_str += str(self.print_symbol) * self.width
            if n < self.height - 1:
                rect_str += '\n'

        return rect_str

    def __repr__(self):
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
