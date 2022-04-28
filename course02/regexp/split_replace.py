#!/usr/bin/env python3
import re

split = re.split(r"[.?!]", "One sentence. Another one? And the last one!")
print(split)

split = re.split(r"([.?!])", "One sentence. Another one? And the last one!")
print(split)

re_sub = re.sub(r"[\w.%+-]+@[\w.-]+", "[HIDDEN]", "Received an email for e.mail@domain.com")
print(re_sub)

re_sub = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(re_sub)
