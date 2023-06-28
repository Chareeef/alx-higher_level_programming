#!/usr/bin/python3
'''
Write a class Square that defines a square by:
* Private instance attribute: size
    - property 'def size(self):' to retrieve it
    - property setter 'def size(self, value):' to set it
* Instantiation with optional size (with type and value verifications)
* Public instance method: 'def area(self):' that returns the square area
* Public instance method: 'def my_print(self):' that prints in stdout
the square with the character #
'''


class Square:
    '''A Square with 'size' as private instance attribute,
    getter and setter properties, and 'area' method'''

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        '''Getter and Setter of the square size'''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('value must be an integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Returns the square area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character #'''
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print('#', end='')
                print()
