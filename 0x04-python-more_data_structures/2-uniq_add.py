#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_add = set(my_list)
    result = sum(uniq_add)
    print("Result: {:g}".format(result))
