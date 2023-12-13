import re

# Function to check if a given word is present in a text
def check_word(word, text):
    return bool(re.search(fr'\b{re.escape(word)}\b', text))

# Function to check if a string contains at least one digit
def check_digit(s):
    return bool(re.search(r'\d', s))

# Function to replace spaces in a string with hyphens
def remove_space(s):
    return re.sub(r'\s', '-', s)

# Function to validate a phone number format (e.g., 99-999-999-99)
def phone_number(phone_number):
    return bool(re.match(r'\d{2}-\d{3}-\d{3}-\d{2}', phone_number))

# Function to validate an email address format
def email(email):
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))
