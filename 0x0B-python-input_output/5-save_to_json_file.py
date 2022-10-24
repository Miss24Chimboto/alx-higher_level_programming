#!/usr/bin/python3
"""
Contains the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w+') as f:
        # serialize to a file
        json.dump(my_obj, f)
