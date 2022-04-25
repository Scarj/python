#!/usr/bin/env python3
import os

print(os.getcwd())
new_dir = "new_dir"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)

os.chdir(new_dir)
print(os.getcwd())
os.chdir("..")

if os.path.exists(new_dir) and os.path.isdir(new_dir):
    os.rmdir(new_dir)

data_dir = "data"
print(os.listdir(data_dir))

current_dir = "."
for file_name in os.listdir(current_dir):
    fullname = os.path.join(current_dir, file_name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
