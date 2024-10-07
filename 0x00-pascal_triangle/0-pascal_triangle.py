#!/usr/bin/env python
"""
'0-pascal_triangle' creates a function that generate a Pascal triangle
"""


def pascal_triangle(n):
    """Generates a list representation of a Pascal triangle
    Args:
        n: Integer defining the size of the triangle.
    Return:
        triangle: A list of list representing Pascal's triangle.
    """
    # Declare the return variable 'triangle'
    triangle = []

    # Return an empty list if n is less than 0
    if (n < 0) return []

    # Handle cases where input is 0
    if (n == 0) return [1]

    # Implement Pascal's Triangle logic
    return triangle
