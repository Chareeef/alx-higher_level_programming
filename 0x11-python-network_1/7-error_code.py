#!/usr/bin/python3
'''
Script that takes in a URL,
sends a request to the URL,
and displays the body of the response
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        response = requests.get(argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.HTTPError:
        print('Error code:', response.status_code)
