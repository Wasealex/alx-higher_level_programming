#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_key = None
    sorted_value = sorted(a_dictionary.values())
    best_value = sorted_value[-1]
    for key, value in a_dictionary.items():
        if value == best_value:
            best_key = key
            break
    return best_key
