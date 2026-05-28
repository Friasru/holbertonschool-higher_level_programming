#!/usr/bin/python3
"""Module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from rectangle"""
    def __init__(self, size):
        self.integer_valid("size", size)
        super().__init__(size, size)
