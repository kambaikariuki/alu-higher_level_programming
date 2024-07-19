#!/usr/bin/python3
"""
creates an object from a "JSON file"
"""


import json

def load_from_json_file(filename):
    '''
    module load_from_json_file
    returns corresponding Python object
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
