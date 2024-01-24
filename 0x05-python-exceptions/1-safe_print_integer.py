#!/usr/bin/python3

def safe_print_integer(value):
    try:
        for i in value:
            if isinstance(value, int):
                print("{:d}".format(value))
                return True
    except TypeError:
        pass
    finally:
        print(end='')

    return False
