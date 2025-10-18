
#!/usr/bin/env python3
"""Mutant ID: 03 - No division (sum only)

Description: Return the sum only (no averaging).

This mutant is a modified variant of the average calculator used for mutation testing.
"""
from typing import List, Iterable
import math, random

def parse_number_list(s: str):
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(tok) for tok in tokens]

def mutated_average(numbers: Iterable[float]) -> float:
    nums = list(numbers)
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list.")
    total = sum(nums)

    # return final value
    return total


def main():
    s = input("Enter numbers (comma/space separated): ").strip()
    nums = parse_number_list(s)
    print("Stored numbers (original):", nums)
    try:
        result = mutated_average(nums)
        print("Mutant result:", result)
    except Exception as e:
        print("Mutant raised an exception:", e)

if __name__ == "__main__":
    main()
