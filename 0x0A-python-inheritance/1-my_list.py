#!/usr/bin/python3
"""
print_sorted: function to be called"""


class MyList(list):
    """
    a subclass of list that init and sort the list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
