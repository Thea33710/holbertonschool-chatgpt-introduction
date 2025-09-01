#!/usr/bin/env python3
import sys

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <nombre_entier>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError:
        print("Erreur: veuillez entrer un nombre entier valide.")
        sys.exit(1)
