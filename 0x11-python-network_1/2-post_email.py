#!/usr/bin/python3
'''
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
'''

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    params = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    req = urllib.request.Request(argv[1], data=params, method='POST')

    with urllib.request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
