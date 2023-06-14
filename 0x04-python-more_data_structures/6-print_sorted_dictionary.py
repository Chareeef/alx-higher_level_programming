#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x, y in dict(sorted(a_dictionary.items())).items():
        print(f'{x}: {y}')
