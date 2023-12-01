#!/usr/bin/python3
'''
Script that takes a GitHub user credentials (username and password),
and uses the GitHub API to display his id
'''

if __name__ == '__main__':
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    user = argv[1]
    token = argv[2]

    url = f'https://api.github.com/user'
    auth = HTTPBasicAuth(user, token)

    response = requests.get(url, auth=auth)

    json_dict = response.json()

    print(json_dict.get('id'))
