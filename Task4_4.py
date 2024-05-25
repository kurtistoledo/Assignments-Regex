# Lesson 4: Python Dictionaries
# 4. Python Regex Challenge: Enhancing E-Commerce Operations

import re

# Product descriptions
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# Keyword tags
keyword_tags = {
    "Smartphone": "Electronics",
    "Cotton t-shirt": "Apparel",
    "Stainless steel kitchen knife set": "Home & Kitchen"
}

# Tag each product based on keywords in the description
for desc in descriptions:
    for keyword, tag in keyword_tags.items():
        if keyword.lower() in desc.lower():
            print(f"Product: {desc} | Tag: {tag}")

# Convert price formats to 'USD XX.XX'
def format_price(match):
    price = match.group(0)
    return f"USD {price}"

# Example price format: "29.99"
price_format = r"\d+\.\d+"
formatted_descriptions = [re.sub(price_format, format_price, desc) for desc in descriptions]

print("\nFormatted Descriptions:")
for formatted_desc in formatted_descriptions:
    print(formatted_desc)
