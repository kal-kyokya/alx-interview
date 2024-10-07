#!/usr/bin/python3
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
    # Initialize a list of n element to be used as return value
    triangle = [0 for i in range(n)]

    # Return an empty list if n is less than 0
    if (n < 0):
        return []

    # Handle cases where input is 0
    if (n == 0):
        return [1]

    # Handle cases where input is 1
    if (n == 1):
        return [1, 1]

    # Implementing Pascal's Triangle logic:
    # Initialize the first two rows
    triangle[0] = [1]
    triangle[1] = [1, 1]

    # Keep track of the row being processed currently
    current = 2

    # Loop through all rows of the triangle
    while (current < n):
        size = current + 1
        row = [0 for i in range(size)]
        row[0] = row[-1] = 1

        # Track the row element's indices
        forward = 1
        backward = -2

        # Loop through the row
        previous = triangle[current - 1]
        while (forward <= size/2):
            row[forward] = previous[forward - 1] + previous[forward]
            row[backward] = row[forward]

            forward += 1
            backward -= 1

        triangle[current] = row
        current += 1

    return triangle
