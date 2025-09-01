#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # On décrémente n pour éviter la boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError("Le nombre doit être non négatif")
    except ValueError as e:
        print("Erreur :", e)
        sys.exit(1)

    f = factorial(num)
    print(f)