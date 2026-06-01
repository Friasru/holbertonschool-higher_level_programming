#!/usr/bin/python3
"""Module for writing a string and returning the number of characters"""


def write_file(filename="", text=""):
    """writes a string and returns number of characters"""
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)

