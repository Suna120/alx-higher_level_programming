#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = list(set(my_list)) 
    result = 0
    for i in range(0, len(uniq)):
        result += uniq[i]
    return result
uniq_add()