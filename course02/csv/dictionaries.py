#!/usr/bin/env python3
import csv

with open("data/software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
         {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
         {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

with open("data/by_department.csv", "w") as department:
    keys = ["name", "username", "department"]
    writer = csv.DictWriter(department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
