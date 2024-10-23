#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 'a'
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = None
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
n = 4.0
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 14
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 16
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 22
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 25
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 38
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 62
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 972
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
