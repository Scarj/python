#!/usr/bin/env python3
import csv
import re


def contains_domain(address, domain):
    domain_pattern = r"[\w \.-]+@" + domain + '$'
    return re.match(domain_pattern, address)


def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r"" + old_domain + "$"
    return re.sub(old_domain_pattern, new_domain, address)


def main():
    old_domain, new_domain = "abc.edu", "xyz.edu"
    csv_file_location = "data/user_email.csv"
    report_file_location = "data/updated_user_email.csv"

    with open(csv_file_location, "r") as f:
        user_data_list = list(csv.reader(f))
        email_key = " " + "Email Address"
        email_index = user_data_list[0].index(email_key)
        print(email_index)
        for user in user_data_list[1:]:
            print(user)
            user_email = user[email_index]
            if contains_domain(user_email, old_domain):
                user[email_index] = replace_domain(user_email, old_domain, new_domain)
            print(user)
        f.close()

    with open(report_file_location, "w+") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()
