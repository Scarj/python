#!/usr/bin/env python3
import csv

file = open("data/csv_file.csv")
csv_file = csv.reader(file)

for row in csv_file:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

file.close()
