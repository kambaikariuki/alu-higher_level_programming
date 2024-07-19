#!/usr/bin/python3
'''
writes object to a text file, using JSON rep
'''
import json


def save_to_json_file(my_obj, filename):
    ''' module save_to_json_file
    accepts Python object and sends JSON representation to file
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
