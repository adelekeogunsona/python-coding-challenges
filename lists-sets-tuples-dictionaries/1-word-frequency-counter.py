#!/usr/bin/python3

# Check if a letter is valid using ASCII values
def is_valid_letter(char):
    char_code = ord(char)
    return char_code == 32 or 65 <= char_code <= 90 or 97 <= char_code <= 122


# Check if it's a string
while True:
    try:
        u_string = str(input("Input: "))
        break
    except Exception:
        print("Enter a valid input")

# Remove anything except letters
new_string = ''
for i in range(len(u_string)):
    if is_valid_letter(u_string[i]):
        new_string += u_string[i]

# Convert to lower case
low_string = new_string.lower()

# Split the text
list_string = low_string.split()

# Turn the list to dictionary with value as 0
dict_string = {key: 0 for key in list_string}

# Get the frequency of each word
for a in list_string:
    dict_string[a] += 1

# Sort the dictionary by key
clean_dict = dict(sorted(dict_string.items()))

# Sort the dictionary by value in desc order
result = dict(sorted(clean_dict.items(), key=lambda x: x[1], reverse=True))

# Print the result
print("Word Frequency:")
for key, value in result.items():
    print("{}: {}".format(key, value))
