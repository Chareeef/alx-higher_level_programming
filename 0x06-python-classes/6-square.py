#!/usr/bin/python3
'''
Write a class Square that defines a square by:
* Private instance attribute: size & position with their getters and setters
* Instantiation with optional size  and position (with type and value verifications)
* Public instance method: 'def area(self):' that returns the square area
* Public instance method: 'def my_print(self):' that prints in stdout
the square with the character '#' taking into account its position
'''


class Square:
    '''A Square with 'size' as private instance attribute,
    getter and setter properties, and 'area' method'''

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        elif not isinstance(position, tuple):
            raise TypeError('must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('must be a tuple of 2 positive integers')
        x, y = position
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('must be a tuple of 2 positive integers')
        elif x < 0 or y < 0:
            raise TypeError('must be a tuple of 2 positive integers')

        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Getter and Setter of the square size'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        '''Getter and Setter of the square position'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('must be a tuple of 2 positive integers')
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('must be a tuple of 2 positive integers')
        elif x < 0 or y < 0:
            raise TypeError('must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        '''Returns the square area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints in stdout the square with the character '#'
        taking into account its position'''
        if self.size == 0:
            print()
        else:
            for down in range(self.position[1]):
                print()
            for lines in range(self.size):
                for right in range(self.position[0]):
                    print(end=" ")
                for columns in range(self.size):
                    print('#', end='')
                print()
