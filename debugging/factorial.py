#!/usr/bin/env python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError as e:
        print("Erreur:", e)
        sys.exit(1)