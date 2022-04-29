#!/usr/bin/env python3
import subprocess

result = subprocess.run(["date"])
print(result)

result = subprocess.run(["sleep", "1"])
print(result)

result = subprocess.run(["ls", "qwe.asd"])
print(result)
