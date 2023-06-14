#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) < 1:
        return None
    sorted_values = sorted(a_dictionary.values())  # crescent order
    big_value = sorted_values[len(sorted_values) - 1]

    for key, val in a_dictionary.items():
        if val == big_value:
            return key
    return None
