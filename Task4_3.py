# Lesson 4: Python Dictionaries
# 3. Advanced Text Processing with Python Regex

import re

def extract_value_by_key(text, key):
    pattern = re.compile(rf"{key}:\s*(.*?)(?=\s*;|$)")
    match = pattern.search(text)
    if match:
        return match.group(1)
    else:
        return None

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key_to_extract = "Occupation"
occupation = extract_value_by_key(text, key_to_extract)

if occupation:
    print(f"{key_to_extract}: {occupation}")
else:
    print(f"{key_to_extract} not found in the text.")
