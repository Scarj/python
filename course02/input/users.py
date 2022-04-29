#!/usr/bin/env python3
import re
import sys

if len(sys.argv) > 1:
    logfile = sys.argv[1]
else:
    logfile = "data/syslog"

usernames = {}

with open(logfile) as file:
    for line in file:
        if "CRON" in line:
            pattern = r"USER \((\w+)\)$"
            result = re.search(pattern, line)
            if result is not None:
                name = result[1]
                usernames[name] = usernames.get(name, 0) + 1

print(usernames)
