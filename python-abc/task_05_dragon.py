#!/usr/bin/python3
"""Module for mixins and Dragon class"""


class SwimMixin:
    """Mixin class that provides wimming ability"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """class that provides flyinh ability"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
