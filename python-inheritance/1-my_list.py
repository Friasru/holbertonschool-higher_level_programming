#!/usr/bin/python3
"""Module for Mylist class"""


class MyList(list):
    """A class that inherits from list with a print_sorted"""
    def print_sorted(self):
        print(sorted(self))
