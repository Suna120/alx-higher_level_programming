#!/usr/bin/python3
def best_score(a_dictionary):
    best = max(a_dictionary.keys(), key=lambda k: a_dictionary[k])
    if 'value' in a_dictionary:
        return a_dictionary[best]
    else:
        return 'None'    
    