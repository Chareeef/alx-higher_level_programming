#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys


if __name__ == '__main__':
    file_size = 0
    status = {'200': 0,
              '301': 0,
              '400': 0,
              '401': 0,
              '403': 0,
              '404': 0,
              '405': 0,
              '500': 0
              }

    try:
        while True:

            for n in range(10):
                splitted_line = sys.stdin.readline().split()
                file_size += int(splitted_line[-1])
                if splitted_line[-2] in status:
                    status[splitted_line[-2]] += 1

            print('File size:', file_size)

            for k, v in status.items():
                if v > 0:
                    print(f'{k}: {v}')

    except KeyboardInterrupt:
        print('File size:', file_size)

        for k, v in status.items():
            if v > 0:
                print(f'{k}: {v}')
