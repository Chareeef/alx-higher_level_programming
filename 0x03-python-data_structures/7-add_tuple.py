#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first, second = 0, 0
    if len(tuple_a) >= 1:
        first += tuple_a[0]
    if len(tuple_b) >= 1:
        first += tuple_b[0]

    if len(tuple_a) >= 2:
        second += tuple_a[1]
    if len(tuple_b) >= 2:
        second += tuple_b[1]

    return (first, second)
