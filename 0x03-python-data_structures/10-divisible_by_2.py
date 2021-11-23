#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_list = []
    for i in my_list:
        if i % 2:
            boolean_list = boolean_list + False
        else:
            boolean_list = boolean_list + True
    return boolean_list