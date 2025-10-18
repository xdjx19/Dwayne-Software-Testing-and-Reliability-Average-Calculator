#!/usr/bin/env python3
"""Mutant ID: 11 - Add 1 to final output"""

from typing import Iterable

def parse_number_list(s: str):
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(tok) for tok in tokens]

def mutated_average(numbers: Iterable[float]) -> float:
    nums = list(numbers)
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list.")
    total = sum(nums)+1
    denom = len(nums)
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
