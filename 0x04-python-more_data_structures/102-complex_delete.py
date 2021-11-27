#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()
    del copy[value]
    return copy
