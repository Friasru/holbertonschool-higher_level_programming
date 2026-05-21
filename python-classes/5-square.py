#!/usr/bin/python3
"""Module for a square class with printing capability"""

class Square:
    """A square defined by its size with area and printing"""
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
