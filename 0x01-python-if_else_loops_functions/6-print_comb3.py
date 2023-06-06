#!/usr/bin/python3

for i in range(0, 89):
    if int(i / 10) < (i % 10):
        print('{:02}, '.format(i), end='')
print(89)
