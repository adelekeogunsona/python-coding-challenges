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
    if len(my_string) > 1:
        clean_string = sanitizer(my_string)
        reverse = clean_string[::-1]
        if clean_string == reverse:
            return True
    return False


# test cases
assert is_palindrome("racecar") == True
assert is_palindrome("Hello") == False
assert is_palindrome("A man, a plan, a canal, Panama!") == True
assert is_palindrome("") == False
assert is_palindrome("a") == False
assert is_palindrome("ab") == False
assert is_palindrome("aa") == True
assert is_palindrome("A Santa at NASA") == True
