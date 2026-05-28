#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class with area and integer_validator methods"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0.format(name)")
