#!/usr/bin/python3
"""ALX Interview"""


def minOperations(n):
    """Min Operations Function"""
    if n <= 1:
        return 0  # Impossible to achieve

    operations = 0
    current = 1  # Start with a single 'H' in the file
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 1  # Copy All operation
        current += clipboard
        operations += 1  # Paste operation

    return operations
