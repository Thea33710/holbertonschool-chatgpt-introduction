#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcule le factoriel d'un entier non négatif n de manière itérative.
    """
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
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Le nombre doit être positif ou nul.")
        f = factorial(number)
        print(f)
    except ValueError as e:
        print("Erreur :", e)
        sys.exit(1)