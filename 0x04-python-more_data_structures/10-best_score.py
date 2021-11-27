#!/usr/bin/python3
def best_score(a_dictionary):
    #best = max(a_dictionary.keys(), key=lambda k: a_dictionary[k])
    if a_dictionary:
        return max(a_dictionary, key = a_dictionary.get)
    else:
        return None    
