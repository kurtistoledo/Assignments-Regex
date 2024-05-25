# Lesson 4: Python Dictionaries
# 2. Python Regular Expressions Deep Dive

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+(?<!exclude\.com)\.[A-Za-z]{2,}", text)
print(emails)