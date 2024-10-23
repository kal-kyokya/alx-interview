#!/usr/bin/python3
"""
'0-minoperations' contains a ITERATIVE function meant to manipulate a file
containing a single character using ['Copy All', 'Paste'] and
end up populating it with a user defined number 'n' of character
"""
import random
from typing import Any, List, Optional


def minOperations(n: int) -> int:
    """Computes the minimum number of operations
    to fill a text file with exactly n characters
    using only 'Copy All' and 'Paste'.
    """
    # Checks the input as a: Positive, Non-zero, Integer
    if not isinstance(n, int) or n <= 0:
        return (0)

    # Edge case for 1: no operations are needed
    if n == 1:
        return 0

    # Initialize variable for the minimum number of operations
    operations = 0

    # Factorize n by dividing it by its smallest factors
    # and accumulate the operations required for each factor
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
