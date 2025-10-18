
#!/usr/bin/env python3
"""Mutant ID: 16 - Convert negatives to positive

Description: Use absolute value for each input.

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
    # convert negatives to positives
    pos = [abs(x) for x in nums]
    total = sum(pos)
    denom = len(pos)

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
