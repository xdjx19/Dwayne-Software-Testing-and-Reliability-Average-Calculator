#!/usr/bin/env python3
"""
Usage:
 - Enter values separated by spaces or commas:
     1 2 3
     or
     1,2,3
 - Enter 'quit' or leave blank to exit.
"""

from typing import List, Iterable
import math
import random

# --- Parsing & Average ---
def parse_number_list(s: str) -> List[float]:
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(tok) for tok in tokens]

def average(numbers: Iterable[float]) -> float:
    nums = list(numbers)
    if len(nums) == 0:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(nums) / len(nums)

# --- Metamorphic relation helpers ---
def scale_inputs(numbers: Iterable[float], k: float) -> List[float]:
    return [x * k for x in numbers]

def permute_inputs(numbers: Iterable[float], seed: int = None) -> List[float]:
    arr = list(numbers)
    rnd = random.Random(seed)
    rnd.shuffle(arr)
    return arr

def approx_equal(a: float, b: float, tol: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)

def verify_scaling_mr(func, original: Iterable[float], k: float, tol: float = 1e-9) -> bool:
    orig_avg = func(original)
    scaled_avg = func(scale_inputs(original, k))
    return approx_equal(scaled_avg, k * orig_avg, tol)

def verify_permutation_mr(func, original: Iterable[float], seed: int = None, tol: float = 1e-9) -> bool:
    """
    Proper permutation MR:
    - Returns True if the function is NOT sensitive to order (average unchanged after shuffle)
    - Returns False if the function is order-sensitive (average changed)
    """
    permuted = permute_inputs(original, seed)
    return approx_equal(func(original), func(permuted), tol)

# --- Interactive Calculator ---
def interactive_calculator():
    print("Average Calculator")
    print("Enter numbers separated by spaces or commas (e.g. '1 2 3' or '1,2,3').")
    print("Type 'quit', 'done', or press Enter to exit.\n")

    while True:
        s = input("Enter numbers: ").strip()
        if s.lower() in ("quit", "done", ""):
            print("Exiting. Goodbye!")
            break
        try:
            nums = parse_number_list(s)
            if not nums:
                print("No numbers parsed. Try again.\n")
                continue

            avg_value = average(nums)
            print(f"Stored numbers: {nums}")
            print(f"Average: {avg_value}\n")

            # --- MR examples ---
            k = 2.0
            scaling_ok = verify_scaling_mr(average, nums, k)
            print(f"Scaling MR (multiply inputs by {k}) holds? -> {scaling_ok}")

            permutation_ok = verify_permutation_mr(average, nums, seed=42)
            permuted = permute_inputs(nums, seed=42)
            print(f"Permutation MR (reorder) holds? -> {permutation_ok} (permuted: {permuted})\n")

        except ValueError as e:
            print(f"Input error: {e}. Enter only numbers separated by spaces or commas.\n")

if __name__ == "__main__":
    interactive_calculator()