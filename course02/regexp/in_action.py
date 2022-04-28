#!/usr/bin/env python3
import re


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ]*[.!?]$", text)
    return result is not None


print(re.search("A.*a", "Argentina"))
print(re.search("A.*a", "Azerbaijan"))
print(re.search("^A.*a$", "Azerbaijan"))
print(re.search("^A.*a$", "Australia"))

variable_pattern = "^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(variable_pattern, "_this_is_valid_variable_name"))
print(re.search(variable_pattern, "my_variable_001"))
print(re.search(variable_pattern, "2my_variable_001"))

print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True
