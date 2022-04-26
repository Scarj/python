#!/usr/bin/env python3
import csv


def read_employees(csv_file_location):
    csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")
    employee_list = []
    for employee in employee_file:
        employee_list.append(employee)
    return employee_list


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["department"])
    department_data = {}

    for department in set(department_list):
        department_data[department] = department_list.count(department)
    return department_data


def write_report(dictionary, report_file):
    with open(report_file, "w") as file:
        for key in sorted(dictionary):
            file.write("{}:{}\n".format(key, dictionary[key]))


employees = read_employees("data/by_department.csv")
print(employees)
departments = process_data(employees)
print(departments)
write_report(departments, "data/report.txt")
