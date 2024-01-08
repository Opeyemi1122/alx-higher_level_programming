#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = (my_list.insert(-2, (new_element)))
        del my_list[-2]
        return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = replace_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
