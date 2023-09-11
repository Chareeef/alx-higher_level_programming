#!/usr/bin/python3
'''This module contains MyInt class, inheriteing from int'''


class MyInt(int):
    '''A derived class from int
    MyInt is a rebel, ithas == and != operators inverted
    '''

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
