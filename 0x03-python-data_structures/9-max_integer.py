#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort()
    last_position = (len(my_list) - 1)
    return my_list[last_position]
