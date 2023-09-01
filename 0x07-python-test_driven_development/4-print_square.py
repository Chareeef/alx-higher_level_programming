#!/usr/bin/python3
"""
Implementation of 4-print_square
Tested with tests/4-print_square.txt
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): the square array's size
    """

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
