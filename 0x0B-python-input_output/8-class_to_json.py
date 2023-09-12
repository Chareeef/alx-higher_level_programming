#!/usr/bin/python3
'''This module contains the class_to_json() function implementation'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure
    for JSON serialization of an object

    Arguments:
        obj: a class instance

    Returns:
        The dictionary description
    '''
    return obj.__dict__


if __name__ == '__main__':
    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number=4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            return "[MyClass] {} - {:d} > {:d}".format(self.__name,
                                                       self.number, self.score)

    m = MyClass("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
