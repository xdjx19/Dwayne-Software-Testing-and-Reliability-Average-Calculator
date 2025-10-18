
#!/usr/bin/env python3
"""Mutant ID: 15 - Ignore zeros

Description: Filter out zero values before averaging.

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
    # filter out zeros
    filtered = [x for x in nums if x != 0]
    if len(filtered) == 0:
        raise ValueError('All values were zero or list empty for this mutant')
    total = sum(filtered)
    denom = len(filtered)

    # return final value
    return total / denom


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
