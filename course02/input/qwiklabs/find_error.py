#!/usr/bin/env python3
import re
import sys


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []

    error_patterns = ["error"]
    for e in error.split(" "):
        error_patterns.append(r"{}".format(e.lower()))

    with open(log_file, "r", encoding='UTF-8') as file:
        for line in file.readlines():
            if all(re.search(error_pattern, line.lower()) for error_pattern in error_patterns):
                returned_errors.append(line)

    return returned_errors


def file_output(returned_errors):
    with open("../data/errors_found.log", "w") as file:
        for error in returned_errors:
            file.write(error)


if __name__ == '__main__':
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
