#!/usr/bin/env python3
import re

log = "July 31 05:54:34 my.computer bad_process[1234567890]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index + 1:index + 6])

pattern = r"\[(\d+)\]"
result = re.search(pattern, log)
print(result[1])

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
