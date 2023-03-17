#!/usr/bin/python3

# merges two dictionaries
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    result = {}
    for key1, value1 in dict1.items():
        result[key1] = value1
    for key2, value2 in dict2.items():
        result[key2] = value2
    return result


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 3, 'c': 4}

dict1 = {}
dict2 = {'a': 1, 'b': 2}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2}
