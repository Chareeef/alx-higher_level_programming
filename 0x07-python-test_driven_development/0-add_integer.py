#!/usr/bin/python3
"""
Implementation of 0-add_integer
Tested with tests/0-add_integer.txt
"""


def add_integer(a, b=98):
    """
    Add two numbers (casted to int)

    Returns: The sum
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
