#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length < 1:
        return None
    max_list = my_list[0]
    for i in range(1, length):
        if max_list < my_list[i]:
            max_list = my_list[i]
    return max_list
