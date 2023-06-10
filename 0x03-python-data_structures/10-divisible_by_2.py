#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_even_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            is_even_list.append(True)
        else:
            is_even_list.append(False)
    return is_even_list
