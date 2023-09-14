#!/usr/bin/python3
'''This module contains the Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class

    Instance Attributes:
        width (int)
        height (int)
        x (int)
        y (int)
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        '''Getter and Setter for width'''
        return self.__width

    @width.setter
    def width(self, new_width):
        self.__width = new_width

    @property
    def height(self):
        '''Getter and Setter for height'''
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def x(self):
        '''Getter and Setter for x'''
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        '''Getter and Setter for y'''
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y
