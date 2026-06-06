#!/usr/bin/python3
"""Module that converts a class instance to a JSON dictionary"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure fron JSON"""
    return obj.__dict__
