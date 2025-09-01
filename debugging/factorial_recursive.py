#!/usr/bin/python3
import sys

# Function description:
# Calculate the factorial of a non-negative integer n using recursion.
# Parameters:
# n (int): A non-negative integer whose factorial is to be computed.
# Returns:
# int: The factorial of n (n!).


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
