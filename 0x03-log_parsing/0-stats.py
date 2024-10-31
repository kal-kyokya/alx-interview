#!/usr/bin/python3
"""
'0-stats' Parses the standard input to generate a report.
"""
from sys import stdin


for line in stdin:
    print(line.split()[0])
