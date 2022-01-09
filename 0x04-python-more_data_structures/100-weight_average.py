#!/usr/bin/python3
def weight_average(my_list=[]):
    average = [sum(x) / len(x) for x in zip(*my_list)]
    if my_list:
        return average(my_list)
    else:
        return 0         
