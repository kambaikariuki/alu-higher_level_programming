#!/usr/bin/python3
"""
obj is an instance of an inherited class,otherwise False
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited \
    from the specified class; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
