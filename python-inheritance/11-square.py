#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

def __str__(self):
        w = self._Rectangle__width
        h = self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
