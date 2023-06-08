#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    args = len(argv) - 1

    print(args, end=' ')

    if args == 1:
        print('argument', end='')
    else:
        print('arguments', end='')

    if args == 0:
        print('.')
    else:
        print(':')
        for i in range(1, args + 1):
            print(f'{i}: {argv[i]}')
