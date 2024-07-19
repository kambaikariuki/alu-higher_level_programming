#!/usr/bin/python3
"""
writes a string to a text file
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
