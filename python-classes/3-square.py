#!/usr/bin/python3
"""Module for a square class with area calculation"""


class Square:
    """A square defined by its size with area calculation"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        return self.__size * self.__size
