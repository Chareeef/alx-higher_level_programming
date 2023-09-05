#!/usr/bin/python3
'''A module within we create a locked class'''


class LockedClass:
    '''A class that prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is called first_name.

    >>> lc = LockedClass()
    >>> lc.first_name = 'jad'
    >>> print('Success :', lc.first_name)
    Success : jad

    >>> try:
    ...     lc.last_name = 'L'
    ... except AttributeError as e:
    ...     print(f'[{e.__class__.__name__}] {e}')
    [AttributeError] 'LockedClass' object has no attribute 'last_name'
    '''

    __slots__ = ('first_name', )
