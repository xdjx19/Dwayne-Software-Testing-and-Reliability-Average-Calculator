#!/usr/bin/env python3
from typing import List, Iterable
import math
import random

# --- Core Average Calculator ---

def parse_number_list(s: str) -> List[float]:
    """Parse string input into list of floats."""
    if not s:
        return []
    tokens = s.replace(",", " ").split()
    return [float(tok) for tok in tokens]

def average(numbers: Iterable[float]) -> float:
    """Compute the average of a list of numbers."""
    nums = list(numbers)
    if not nums:
        raise ValueError("Cannot compute average of an empty list.")
    return sum(nums) / len(nums)

# --- Metamorphic Relation Helpers ---

def scale_inputs(numbers: Iterable[float], k: float) -> List[float]:
    """Multiply each element by k."""
    return [x * k for x in numbers]

def permute_inputs(numbers: Iterable[float], seed: int = None) -> List[float]:
    """Return a shuffled copy of the list for permutation MR."""
    arr = list(numbers)
    rnd = random.Random(seed)
    rnd.shuffle(arr)
    return arr

def approx_equal(a: float, b: float, tol: float = 1e-9) -> bool:
    """Floating-point tolerant comparison."""
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)

def verify_scaling_mr(original: Iterable[float], k: float, tol: float = 1e-9) -> bool:
    """Check scaling MR: average(scale(inputs, k)) == k * average(inputs)"""
    return approx_equal(average(scale_inputs(original, k)), k * average(original), tol)

def verify_permutation_mr(original: Iterable[float], permuted: Iterable[float], tol: float = 1e-9) -> bool:
    """Check permutation MR: average(permuted) == average(original)"""
    return approx_equal(average(original), average(permuted), tol)

# --- Interactive CLI ---

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
                print("No numbers parsed. Try again.")
                continue

            avg_value = average(nums)
            print(f"Stored numbers: {nums}")
            print(f"Average: {avg_value}\n")

            # MR examples
            k = 2.0
            print(f"Scaling MR (multiply inputs by {k}) holds? -> {verify_scaling_mr(nums, k)}")
            permuted = permute_inputs(nums, seed=42)
            print(f"Permutation MR (reorder) holds? -> {verify_permutation_mr(nums, permuted)} (permuted: {permuted})\n")

        except ValueError as e:
            print(f"Input error: {e}. Enter only numbers separated by spaces or commas.\n")

if __name__ == "__main__":
    interactive_calculator()