#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        y = 0
        ints = 0

        while y < x:
            if type(my_list[y]) is not int:
                y += 1
                continue
            print('{:d}'.format(my_list[y]), end='')
            y += 1
            ints += 1

        print()
        return ints
    except IndexError:
        raise IndexError
