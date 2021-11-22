#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    def Reverse(lst):
        lst.reverse()
        return lst
    print("{:d}".format(my_list))
