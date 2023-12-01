#!/usr/bin/python3
'''
Script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''

if __name__ == '__main__':
    from sys import argv
    import requests

    if len(argv) > 1:
        data = {"q": argv[1]}
    else:
        data = {"q": ""}

    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        dict_json = response.json()

        if 'id' in dict_json and 'name' in dict_json:
            print('[{}] {}'.format(dict_json['id'], dict_json['name']))
        else:
            print('No result')

    except Exception:
        print('Not a valid JSON')
