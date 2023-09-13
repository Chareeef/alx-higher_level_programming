#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


if __name__ == '__main__':
    import sys

    def print_metrics(file_size, status_codes):
        '''Print formatted metrics'''

        print('File size:', file_size)

        for k in sorted(status_codes):
            if status_codes[k] > 0:
                print(f'{k}: {status_codes[k]}')

    dont_stop = True
    file_size = 0
    status_codes = {'200': 0,
                    '301': 0,
                    '400': 0,
                    '401': 0,
                    '403': 0,
                    '404': 0,
                    '405': 0,
                    '500': 0
                    }

    try:
        while dont_stop:

            n = 0
            while n < 10:
                line = sys.stdin.readline()
                if line == '':
                    dont_stop = False
                    break

                splitted_line = line.split()
                try:
                    file_size += int(splitted_line[-1])
                except (IndexError, ValueError):
                    pass

                try:
                    if splitted_line[-2] in status_codes:
                        status_codes[splitted_line[-2]] += 1
                except IndexError:
                    pass

                n += 1

            print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise
