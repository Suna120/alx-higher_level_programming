#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_character = "None"
    elif len(sentence) !=0 and len(sentence) > 0:
        first_character = sentence[:1]
    return len(sentence), first_character
    