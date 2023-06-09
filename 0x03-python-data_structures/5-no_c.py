#!/usr/bin/python3

# Remove all 'c' and 'C' from a string and return it
def no_c(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] not in ('c', 'C'):
            new_string += string[i]
    return new_string
