#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
            return max
        else:
            return None
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    print("Max:{}".format(max))    