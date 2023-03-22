#!/usr/bin/python3
import re

def find_emails(text: str) -> list:
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    matches = re.findall(pattern, text)
    return matches


text1 = "Please contact us at support@example.com for assistance."
assert find_emails(text1) == ["support@example.com"]

text2 = "The email addresses to contact us are info@example.com and help@example.com"
assert find_emails(text2) == ["info@example.com", "help@example.com"]

text3 = "Invalid emails such as user@.com and @example.com should not be matched."
assert find_emails(text3) == []
