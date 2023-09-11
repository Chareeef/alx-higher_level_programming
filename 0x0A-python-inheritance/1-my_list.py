#!/usr/bin/python3
'''This module implements MyList class for task 1'''


class MyList(list):
    '''A class MyList that inherits from list'''

    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort)'''
        print(sorted(self))
