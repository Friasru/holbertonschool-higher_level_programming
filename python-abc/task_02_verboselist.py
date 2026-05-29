#!/usr/bin/python3
"""Module for Vervoselist that extends the list class"""


class Verboselist(list):
    """Custom list class that prints notifications"""
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        num_items = len(items)
        super().extend(items)
        print(f"Extend the list with [{num_items}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped [{item}] from the list")
        return item
