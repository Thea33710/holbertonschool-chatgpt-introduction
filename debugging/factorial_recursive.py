#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer `n` using recursion.

    Parameters:
    n (int): A non-negative integer

    Returns:
    int: The factorial of `n`

    Raises:
    RecursionError: If `n` is too large and exceeds the recursion limit
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ensure a command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python3 script.py <non-negative-integer>")
    sys.exit(1)

# Convert argument to integer and calculate factorial
try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Number must be non-negative.")
    result = factorial(number)
    print(result)
except ValueError as e:
    print("Error:", e)
    sys.exit(1)