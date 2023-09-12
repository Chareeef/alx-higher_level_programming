#!/usr/bin/python3
'''A script that adds all arguments to a Python list,
and then save them to a file
'''
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    '''Add arguments to a Python list stored in "add_item.json"'''

    filename = 'add_item.json'
    with open(filename, 'a+', encoding='utf-8') as f:
        f.seek(0, 0)
        if f.read() == '':
            f.write('[]')

    json_list = load_from_json_file(filename)
    for item in argv[1:]:
        json_list.append(item)
    save_to_json_file(json_list, filename)


add_item()
