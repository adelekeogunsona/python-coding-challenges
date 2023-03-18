#!/usr/bin/python3

# clean and convert string to lowercase
def sanitizer(my_string: str) -> str:
    result = ''
    for string in my_string:
      letter = ord(string)
      if letter in range(65, 91) or letter in range(97,123):
        result += chr(letter).lower()
      else:
        continue
    return result
    

# check for palindrome
def is_palindrome(my_string: str) -> str:
    if len(my_string) < 2:
      return False
    else:
      clean_string = sanitizer(my_string)
      reverse = clean_string[::-1]
      for i in range(len(reverse)):
        if reverse[i] != clean_string[i]:
          return False
    return True


assert is_palindrome("racecar") == True
assert is_palindrome("Hello") == False
assert is_palindrome("A man, a plan, a canal, Panama!") == True
