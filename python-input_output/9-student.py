#!/usr/bin/python3
"""Module that defines a student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Class that defines a student by first, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        result = ""
        for key, value in self.__dict__.items():
            result += "{} => {} /".format(key, value)
        return result
