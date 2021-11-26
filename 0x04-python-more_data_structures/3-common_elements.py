#!/usr/bin/python3
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl"}

def common_elements(set_1, set_2):
    set_c = [value for value in set_1 if value in set_2]
    return set_c
x = common_elements(set_1, set_2)
print(x, end=" ")