#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is not None:
        for i in range(len(my_list)):
            print('{}'.format(my_list[i]))
