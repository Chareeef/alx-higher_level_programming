#!/usr/bin/python3
'''This module contains the append_after() function implementation'''


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file,
    after each line containing a specific string

    Argument:
        filename (str): the text file name
        search_string (str): the specific string that the line should contain
        new_string (str): string to insert after that line
    '''

    with open(filename, 'r+', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == '':  # End of the file
                return

            if search_string in line:
                # Save last position and a copy of next lines
                last_position = f.tell()
                backup = f.read()

                # Come back to last position
                f.seek(last_position)

                # Append the new string
                f.write(new_string)

                # Rewrite the saved backup
                last_position = f.tell()
                f.write(backup)
                f.seek(last_position)
