#!/usr/bin/python3
"""
Defines an inherited list class MyList
"""


class MyList(list):
    """Inherits from list
    """
    def print_sorted(self):
        """Prints the list in ascending order
        """
        print(sorted(self))
