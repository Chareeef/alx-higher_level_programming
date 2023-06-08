#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    match operator:
        case '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        case '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        case '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        case '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))
        case _:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
