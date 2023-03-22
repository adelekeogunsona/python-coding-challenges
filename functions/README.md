## Challenge 1

**Palindrome Detector**

A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward. For example, "racecar" is a palindrome.

Write a Python function called **is_palindrome** that takes in a string as input and returns True if the string is a palindrome, and False otherwise.

The function should ignore spaces, punctuation, and capitalization when determining if a string is a palindrome. For example, "A man, a plan, a canal, Panama!" should be considered a palindrome.

Your function should be case-insensitive, meaning that "Racecar" and "racecar" should both be considered palindromes.

Example Input/Output:
```
is_palindrome("racecar")
# Returns True

is_palindrome("hello")
# Returns False

is_palindrome("A man, a plan, a canal, Panama!")
# Returns True
```

## Challenge 2
**Email Search using Regex**

Create a function that takes a string of text as input and returns a list of all the email addresses found in the text. The function should use regular expressions to identify valid email addresses.

Function signature:
```
def find_emails(text: str) -> List[str]:
```

Test Cases:
```
text1 = "Please contact us at support@example.com for assistance."
find_emails(text1) => ["support@example.com"]

text2 = "The email addresses to contact us are info@example.com and help@example.com"
find_emails(text2) => ["info@example.com", "help@example.com"]

text3 = "Invalid emails such as user@.com and @example.com should not be matched."
find_emails(text3) => []
```

