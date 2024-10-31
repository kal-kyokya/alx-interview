#!/usr/bin/python3
"""
'0-stats' Parses the standard input to generate a report.
"""
from sys import stdin
from datetime import datetime


# Track the number of lines processed
count = 0

# Track the total file size and status code ratio
total_size = 0
codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_c = {code: 0 for code in codes}

# Isolate and Process each line
for line in stdin:

    # Extract the must-have fields
    ip = line.split()[0]
    dash = line.split()[1]
    date = f"{line.split()[2].strip('[')} {line.split()[3].strip(']')}"
    string = f"{line.split()[4]} {line.split()[5]} {line.split()[6]}"
    status_code = line.split()[7]
    file_size = line.split()[8]

    # Ensure each field adhere to the expected format
    if (len(line.split()) != 9 or dash != '-' or
        string != '"GET /projects/260 HTTP/1.1"' or
        type(int(status_code)) != int or
        type(int(file_size)) != int):
        # Skip this line
        continue

    for num in ip.split('.'):
        if type(int(num)) != int:
            continue

    try:
        datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        continue
    else:
        count += 1
        status_c[status_code] += 1
        total_size += int(file_size)

        if count == 10:
            print("File size: {}".format(total_size))
            for key, value in status_c.items():
                if value and value != 0:
                    print("{}: {}".format(key, value))
            count = 0
