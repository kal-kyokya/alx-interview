#!/usr/bin/python3
"""
Main file for testing
"""

makechange = __import__('0-make_change').makeChange

print(makeChange([], 37))

print(makeChange([1, 2, 25, 37], 0))

print(makeChange([14, 12, 125, 21], -25))

print(makeChange([1, 5, 10, 20, 50, 100], 62))

print(makeChange([1256, 54, 48, 16, 102], 1453))
