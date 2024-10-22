#!/usr/bin/python3
"""
'0-minoperations' contains a function meant to manipulate a file
containing a single character using ['Copy All', 'Paste'] and
end up populating it with a user defined number 'n' of character
"""
import random
from typing import Any, List, Optional


def minOperations(n: int) -> int:
    """Computes the required  minimum amount of operations
    to fill a text file with a number n of characters.
    """
    # Checks the input as [Positive, Non-zero, Integer]
    if not isinstance(n, int) or n <= 0:
        return (0)

    # Handle cases where n is 1
    if n == 1:
        return (0)

    # Handle cases where n is a prime number
    if n in [2, 3, 5] or all([n % 2, n % 3, n % 5]):
        return (n)

    # Process any other value using dynamic programming and memoization
    memoization = [i if (i in [1, 2, 3, 5]) else None for i in range(n + 1)]

    # Cache minimum operations of all values lesser than n
    for count in range(4, n + 1):
        for div in [2, 3, 5]:
            if count % div == 0:
                memoization[count] = div + minOperations(int(count/div))
                break

    return (memoization[n])
