#!/usr/bin/python3

for i in range(ord('Z'), ord('A') - 1, -1):
    if i % 2 == 0:
        i += ord('a') - ord('A')
    print('{}'.format(chr(i)), end='')
