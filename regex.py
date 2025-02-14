import re

def is_number(text):
    pattern = r"^-?\d*(\.\d+)?$"
    match = re.fullmatch(pattern, text)
    return match is not None

# Test cases
print(is_number(""))    

