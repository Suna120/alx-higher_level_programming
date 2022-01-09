#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    """
    first soln to task. 4/9.
    for i in range(len(new_list)) :
        new_list.get(i)
        new_list[i] = new_list[i] * 2
    return new_list"""
    while i != len(my_list):
        if my_list[i] != search:
            new_list.append(my_list[i])
        else:
            new_list.append(replace)
        i += 1
    return new_list
