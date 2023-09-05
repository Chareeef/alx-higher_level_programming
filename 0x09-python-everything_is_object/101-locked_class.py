#!/usr/bin/python3
'''A module within we create a locked class'''


class LockedClass:
    '''A class that prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is called first_name.
    '''

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no " +
                                 f"attribute '{name}'")
        else:
            super().__setattr__(name, value)
