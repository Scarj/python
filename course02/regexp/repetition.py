#!/usr/bin/env python3
import re


def repeating_letter_a(text):
    result = re.search(r"[aA]+.*[aA]+", text)
    return result is not None


print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py[a-z]*n", "Python programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I likes peaches"))
