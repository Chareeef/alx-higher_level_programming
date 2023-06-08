#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    sum_of_args = 0

    for i in range(1, len(argv)):
        sum_of_args += int(argv[i])
    print(sum_of_args)
