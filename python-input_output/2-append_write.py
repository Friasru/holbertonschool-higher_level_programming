#!/usr/bin/python3
"""Module for writing a function to append a string"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.append(text)
