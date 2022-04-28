#!/usr/bin/env python3
import re

log = "July 31 05:54:34 my.computer bad_process[12345]: ERROR Performing package upgrade"
regexp = r"\[(\d+)]"
result = re.search(regexp, log)
print(result[1])

result = re.search(regexp, "A completely different string [654321]")
print(result[1])


def extract_pid(log_line):
    pattern = r"\[(\d+)]"
    search = re.search(pattern, log_line)
    if  search is None:
        return ""
    return search[1]


print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))


def extract_pid_with_status(log_line):
    regex = r"\[(\d+)\].*(\b[A-Z]+)\b"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid_with_status("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid_with_status("99 elephants in a [cage]")) # None
print(extract_pid_with_status("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid_with_status("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
