#!/usr/bin/env python3
import re

search = re.search(r"^(\w*), (\w*)$", "Scherbakov, Evgeniy")
print(search)
s, n = search.groups()
print("{} {}".format(n, s))
print(search[0])
print(search[1])
print(search[2])
print()


def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name("Scherbakov, Evgeniy"))
print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Hopper, Grace M."))
