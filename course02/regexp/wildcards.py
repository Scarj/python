#!/usr/bin/env python3
import re


def check_punctuation(text):
    result = re.search(r"[,'!;?.]", text)
    return result is not None


print(re.search(r"[Pp]ython", "Python"))
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search(r"cloud[a-zA-Z\d]", "cloudy"))
print(re.search(r"cloud[a-zA-Z\d]", "cloud9"))

print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

print(re.search(r"[^a-zA-Z]", "This is sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is sentence with spaces."))
print(re.search(r"dog|cat", "I like cats."))
print(re.search(r"dog|cat", "I like dogs."))
print(re.search(r"dog|cat", "I like dogs and cats."))
print(re.findall(r"dog|cat", "I like both dogs and cats."))
