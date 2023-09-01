#!/usr/bin/python3
"""
Implementation of 3-say_my_name
Tested with tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>"

    Args:
    first_name (string)
    last_name (string)
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/3-say_my_name.txt")
