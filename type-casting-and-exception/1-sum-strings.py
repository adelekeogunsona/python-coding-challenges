#!/usr/bin/python3
def sum_strings(number):
    sum = 0
    for no in number:
        try:
            sum += int(no)
        except ValueError:
            return None
    return sum


# Test Cases
test_1 = ['1', '2', '3']
print(sum_strings(test_1))

test_2 = ['2', '4', '6', '8']
print(sum_strings(test_2))

test_3 = ['1', '2', '3', 'four']
print(sum_strings(test_3))

test_4 = ['0', '-1', '123', '456', '789', '1000', '9999']
print(sum_strings(test_4))
