#!/usr/bin/python3
"""
Contains the "load_from_json_file" function
"""

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" """
    # open file as f
    with open(filename, 'r') as f:
        # load from json
        return json.load(f)
