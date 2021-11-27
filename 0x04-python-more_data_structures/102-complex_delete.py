#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = dict(a_dictionary)
    del x[value]
    return x
