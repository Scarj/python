#!/usr/bin/env python3
import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.local", "10.2.5.6"]]

with open("data/hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
