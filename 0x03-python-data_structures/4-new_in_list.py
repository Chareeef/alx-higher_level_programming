#!/usr/bin/python3

# This function replaces an element in a list at a specific position
# without modifying the original list
def new_in_list(my_list, idx, new_element):
    copy = my_list[:]
    if idx not in range(0, len(my_list)):
        return copy
    copy[idx] = new_element
    return copy
