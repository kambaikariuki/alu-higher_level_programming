#!/usr/bin/python3
"""
Returns True if object is instance of a class that inherited from \
specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is instance of a class that inherited from \
specified class; otherwise False
    """
    return isinstance(obj, a_class)
