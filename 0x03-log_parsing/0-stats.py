#!/usr/bin/python3
"""
'0-stats' Parses the standard input to generate a report.
"""
from sys import stdin
from datetime import datetime
from collections import defaultdict

# Initialize counters
count = 0
total_size = 0
status_c = defaultdict(int)
codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

for line in stdin:
    parts = line.split()

    # Basic validation checks
    if len(parts) != 9 or parts[1] != '-' or\
       parts[4:7] != ['"GET', '/projects/260', 'HTTP/1.1"']:
        continue

    # Field extraction
    string = f"{parts[2].strip('[')} {parts[3].strip(']')}"
    ip, _, date, status_code, file_size = (parts[0], parts[1], string,
                                           parts[7], parts[8])

    # Detailed validations
    try:
        if not all(0 <= int(num) <= 255 for num in ip.split('.')):
            continue
        datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        status_code = str(int(status_code))
        file_size = int(file_size)
    except (ValueError, IndexError):
        continue

    # Update counters
    count += 1
    total_size += file_size
    if status_code in codes:
        status_c[status_code] += 1

    # Print every 10 lines
    if count == 10:
        print(f"File size: {total_size}")
        for code in sorted(codes):
            if status_c[code]:
                print(f"{code}: {status_c[code]}")
        count = 0
