#!/usr/bin/env python3
import subprocess
import sys

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "not_exists.file"], capture_output=True)
print(result.returncode)
print(result.stderr.decode())
