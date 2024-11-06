#!/usr/bin/python3
"""
'0-validate_utf8' contains a python function executing UTF-8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding."""
    expected_bytes = 0
    for byte in data:
        if expected_bytes == 0:
            if (byte >> 5) == 0b110:
                expected_bytes = 1
            elif (byte >> 4) == 0b1110:
                expected_bytes = 2
            elif (byte >> 3) == 0b11110:
                expected_bytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_bytes -= 1
    return expected_bytes == 0
