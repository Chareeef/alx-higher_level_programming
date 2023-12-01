#!/usr/bin/python3
'''
Script that takes a GitHub user credentials (username and password),
and uses the GitHub API to display his id
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    user = argv[1]
    token = argv[2]

    url = f'https://api.github.com/{user}'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)

    json_dict = response.json()

    if 'id' in json_dict.keys():
        print(json_dict['id'])
    else:
        print(None)
