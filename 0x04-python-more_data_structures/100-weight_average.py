#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    for sub in my_list:
        for i in sub:
            sum = sum + i
    result = sum / len (my_list)
    if len(my_list) >= 0:
        print(result)
    elif len < 0:
        print(0)    
        
