#!/usr/bin/python3

def list_stats(lst: list) -> dict:
    even_sum = 0
    odd_sum = 0
    unique_values = set(lst)
    for number in lst:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    
    result = {'even_sum': even_sum, 'odd_sum': odd_sum, 'unique_values': unique_values}
    return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list_stats(lst)
assert result == {'even_sum': 20, 'odd_sum': 25, 'unique_values': {1, 2, 3, 4, 5, 6, 7, 8, 9}}

lst = [2, 4, 6, 8]
result = list_stats(lst)
assert result == {'even_sum': 20, 'odd_sum': 0, 'unique_values': {2, 4, 6, 8}}

lst = [1, 3, 5, 7, 9]
result = list_stats(lst)
assert result == {'even_sum': 0, 'odd_sum': 25, 'unique_values': {1, 3, 5, 7, 9}}
