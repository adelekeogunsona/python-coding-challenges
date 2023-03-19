## Challenge 1

__Two Sum__

Given an array of integers, return the indices of the two numbers that add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Function signature:
```
def two_sum(nums: Array[int], target: int) -> Array[int]:
```

Test case 1:
```
nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == array('i', [0, 1])
```

Test case 2:
```
nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == array('i', [1, 2])
```

Test case 3:
```
nums = [0, 4, 3, 0]
target = 0
assert two_sum(nums, target) == array('i', [0, 3])
```

Test case 4:
```
nums = []
target = 8
assert two_sum(nums, target) == array('i')
```
