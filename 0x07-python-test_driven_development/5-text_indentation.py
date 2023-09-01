#!/usr/bin/python3
"""
Implementation of 5-text_indentation
Tested with tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Print formatted text with two new lines after each of these . : ?
    Every printed line has to be free of spaces at its end and beginning

    Args:
    text (str): text to be formatted
    """

    # Checking text's data type:
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Strip text to avoid leading and trailing spaces:
    stripped_text = text.strip()

    # Initialize Index and defining last_index:
    i = 0
    last_index = len(stripped_text) - 1

    # Return if stripped_text is empty:
    if len(stripped_text) == 0:
        return

    # Looping through every character in stripped_text and printing it:
    while i < len(stripped_text):
        print(stripped_text[i], end='')

        # If the character is one of these (. : ?), print two new lines:
        if stripped_text[i] in ('.', ':', '?'):
            print('\n')

            # Skip next spaces:
            if i < last_index:
                while stripped_text[i + 1] == ' ':
                    i += 1

        # Increment index:
        i += 1


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
