#!/usr/bin/env python3
import os
import datetime

filename = "data/spider.txt"
print(str(os.path.getsize(filename)))
modification_time = os.path.getmtime(filename)
print(modification_time)
print(datetime.datetime.fromtimestamp(modification_time))
print(os.path.abspath(filename))
