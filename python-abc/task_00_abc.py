#!/usr/bin/python3
"""Module for abstract base class example"""


from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
