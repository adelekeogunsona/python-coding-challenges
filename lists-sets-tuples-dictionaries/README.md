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