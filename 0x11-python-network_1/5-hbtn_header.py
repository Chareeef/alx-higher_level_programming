#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found
in the header of the onse.
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    response = requests.get(argv[1])

    print(response.headers['X-Request-Id'])
