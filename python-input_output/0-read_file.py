#!/usr/bin/python3
"""
Function to read text file and print
"""


def read_file(filename=""):
    """Reads text file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
