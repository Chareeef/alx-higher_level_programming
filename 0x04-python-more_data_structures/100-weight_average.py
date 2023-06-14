#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    if my_list == []:
        return 0

    numerator_list = list(map(lambda tup: tup[0] * tup[1], my_list))
    numerator = 0
    for z in numerator_list:
        numerator += z

    denominator = 0
    for (x, y) in list(my_list):
        denominator += y

    weight = numerator/denominator
    return weight
