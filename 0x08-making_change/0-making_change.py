#!/usr/bin/python3
"""
'0-make_change' contains a function solving the 'coin change' problem.
"""


def makeChange(coins: list, total: int) -> int:
    """
    If possible, determines the minimum number of coins
    required to reach the given 'total'.
    """
    # Ensures the requested total is valid
    if total <= 0:
        return (0)

    # Sort the list of denominations for faster manipulation
    sorted(coins)

    # Initialize a set of variables facilitating tracking of progress
    subtotal = operations = 0
    index = len(coins) - 1

    while index >= 0:
        if subtotal == total:
            return (operations)
        if coins[index] > (total - subtotal):
            index -= 1
            continue

        subtotal += coins[index]
        operations += 1

    return (-1)
