#!/usr/bin/python3
from array import *

def two_sum(input_array: array, target: int) -> array:
    output_array = array('i')
    
    for index1, number1 in enumerate(input_array):
        for index2 in range(1, len(input_array)):
            if number1 + input_array[index2] == target:
                output_array.append(index1)
                output_array.append(index2)
                return output_array
    return output_array


nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == array('i', [0, 1])

nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == array('i', [1, 2])

nums = [0, 4, 3, 0]
target = 0
assert two_sum(nums, target) == array('i', [0, 3])

nums = []
target = 8
assert two_sum(nums, target) == array('i')
