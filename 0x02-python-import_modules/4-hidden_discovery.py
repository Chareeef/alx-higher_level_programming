#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    list_h = dir(hidden_4)
    for i in range(0, len(list_h)):
        if list_h[i][0] != '_':
            print(list_h[i])
