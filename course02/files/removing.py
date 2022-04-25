#!/usr/bin/env python3
import os

with open("data/novel.txt", "w") as file:
    file.write("It was a dark and stormy night\n")

if os.path.exists("data/novel.txt"):
    os.rename("data/novel.txt", "data/novel2.txt")

if os.path.exists("data/novel2.txt"):
    os.remove("data/novel2.txt")
