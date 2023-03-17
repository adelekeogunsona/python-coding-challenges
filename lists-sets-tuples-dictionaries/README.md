## Lists, Sets, Tuples and Dictionaries

## Challenge 1

Word Frequency Counter

Write a Python program that takes in a string of text and outputs a dictionary that contains the frequency of each word in the text. Your program should ignore case and punctuation, and treat words with different capitalization as the same word.

Here are the requirements and specifications for your program:

- The program should prompt the user to enter a string of text.
- The program should remove any punctuation marks from the text (e.g., periods, commas, question marks).
- The program should split the text into individual words.
- The program should convert all words to lowercase.
- The program should count the frequency of each word in the text and store the results in a dictionary.
- The program should print out the resulting dictionary, sorted by word frequency (in descending order).
- The program should handle exceptions and errors gracefully.


Here's an example of what the program's output might look like:
```
Input: Hello, world! This is a test. Hello again.

Word frequency:
hello: 2
a: 1
again: 1
is: 1
test: 1
this: 1
world: 1
```

```
Input: Python is a popular programming language, used for data analysis and machine learning. Python 3.0 was released in 2008.

Word Frequency:
python: 2
a: 1
analysis: 1
and: 1
data: 1
for: 1
in: 1
is: 1
language: 1
learning: 1
machine: 1
popular: 1
programming: 1
released: 1
used: 1
was: 1
```

## Challenge 2
Merge Dictionaries

Write a Python function that takes two dictionaries as input and returns a new dictionary that contains all the key-value pairs from both input dictionaries. If the same key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.

Function signature:
```
def merge_dicts(dict1: dict, dict2: dict) -> dict:
    pass
```

Input
```
The input to the function merge_dicts will be two dictionaries, dict1 and dict2. The keys and values in the dictionaries can be of any data type.
```

Output
```
The output of the function merge_dicts will be a new dictionary that contains all the key-value pairs from both input dictionaries. If the same key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.
```

Example
```
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 3, 'c': 4}

dict1 = {}
dict2 = {'a': 1, 'b': 2}
assert merge_dicts(dict1, dict2) == {'a': 1, 'b': 2}
```

## Challenge 3
List Analysis

Write a Python function that takes in a list of integers and returns a dictionary with the following key-value pairs:

"even_sum": the sum of all even integers in the list  
"odd_sum": the sum of all odd integers in the list  
"unique_values": a set containing all unique integers in the list  

Function signature:

```
def list_stats(lst: list) -> dict:
    pass
```

Example:
```
lst = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 9, 8, 10]
result = list_stats(lst)
print(result)  # {'even_sum': 34, 'odd_sum': 25, 'unique_values': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}}
```

Test case 1
```
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list_stats(lst)
assert result == {'even_sum': 20, 'odd_sum': 25, 'unique_values': {1, 2, 3, 4, 5, 6, 7, 8, 9}}
```

Test case 2
```
lst = [2, 4, 6, 8]
result = list_stats(lst)
assert result == {'even_sum': 20, 'odd_sum': 0, 'unique_values': {2, 4, 6, 8}}
```

Test case 3
```
lst = [1, 3, 5, 7, 9]
result = list_stats(lst)
assert result == {'even_sum': 0, 'odd_sum': 25, 'unique_values': {1, 3, 5, 7, 9}}
```