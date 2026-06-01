#!/usr/bin/python3
"""Module for reading and printing file content"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename,"w", encoding='utf-8') as f:
        print(f.read(), end='')
