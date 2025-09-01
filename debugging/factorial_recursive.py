#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Calculates the factorial of a non-negative integer n using recursion.
    The factorial of n (denoted n!) is the product of all positive integers
    less than or equal to n. By definition, factorial of 0 is 1.

    Parameters:
    -----------
    n : int
        A non-negative integer whose factorial is to be computed.

    Returns:
    --------
    int
        The factorial of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid non-negative integer.")
        sys.exit(1)

    f = factorial(num)
    print(f)

if __name__ == "__main__":
    main()