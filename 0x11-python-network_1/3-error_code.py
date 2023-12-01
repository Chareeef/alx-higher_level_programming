#!/usr/bin/python3
'''
Script that takes in a URL,
sends a request to the URL,
and displays the body of the response
'''

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
