#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        char = str[i]
        if ord(char) in range(ord('a'), ord('z') + 1):
            char = chr(ord(char) - ord('a') + ord('A'))
        print('{}'.format(char), end='')
    print()

uppercase("polYuopzZXZZzzz.")
