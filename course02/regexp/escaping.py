#!/usr/bin/env python3
import re


def check_character_groups(text):
    result = re.search(r"\w +\w", text)
    return result is not None


print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "domain.com"))
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
print(re.search(r"\d", "This is 1st example"))

print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False
