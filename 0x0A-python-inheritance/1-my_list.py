#!/usr/bin/python3
"""
print_sorted: function to be called"""


def print_sorted(self):
    """
    a class MyList that inherits from list
    """
    sorted_list = sorted(self)
    print(sorted_list)
    return sorted_list