#!/usr/bin/env python3
import re


def show_time_of_pid(input_line):
    pattern = r"^(\w{3} \d{1,2} \d{2}:\d{2}:\d{2}).*\[(\d+)]"
    result = re.search(pattern, input_line)
    return "{} pid:{}".format(result[1], result[2])


logfile = "data/syslog"
with open(logfile) as file:
    for line in file:
        print(show_time_of_pid(line.strip()))
