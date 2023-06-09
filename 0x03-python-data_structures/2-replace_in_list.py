#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx not in range(len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list



listn = [0, 1, 2, 3]
print(listn)
new = replace_in_list(listn, 1, 0)
print(listn)
print(new)
