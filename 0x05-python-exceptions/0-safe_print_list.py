#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for item in my_list:
        if item is None or y > x:
            break
        print(item, end='')
        y += 1

    print()
    return y
