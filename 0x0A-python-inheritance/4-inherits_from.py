#!/usr/bin/python3
'''This module implements inherits_from() function'''


def inherits_from(obj, a_class):
    '''Returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class ;
    otherwise returns False.'''

    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
